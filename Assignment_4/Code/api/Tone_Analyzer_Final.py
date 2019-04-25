#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, redirect, url_for, request
import requests as rq
import json
from watson_developer_cloud import ToneAnalyzerV3
import operator
from flask_wtf import Form
from wtforms import RadioField
from wtforms import validators, ValidationError

def getResponse(cntry, noOfSongs ):
    # To store the list of tracks and lyrics
    tracks = []
    lyrics = []
    url = []
    
    #base url
    base_url = 'https://api.musixmatch.com/ws/1.1/'

    #apikey
    api_key = '&apikey='

    #format url to form the json response
    format_url = '?format=json&callback=callback'

    #country code fetched from web page
    country = cntry

    #input paramter to fetch the tracks on musixmatch
    parameter = 'chart.tracks.get'
    chart_name= 'top'
    page = 1

    #Total  number of songs
    page_size = noOfSongs
    f_has_lyrics = 1

    #request url 
    api_call = base_url+parameter+format_url+'&chart_name='+chart_name+'&page='+str(page)+'&page_size='+str(page_size)+'&country='+country+'&f_has_lyrics='+str(f_has_lyrics)+api_key
#    print(api_call)

    #response
    response = rq.get(api_call)
    data = response.json()
    data = data['message']['body']
      
    for i in data['track_list']:
        for j in i.values():
            tracks.append(j['track_name'])
#    print(tracks)

    #input paramter to fetch the lyrics on musixmatch
    ly_param = 'track.lyrics.get'

    for k in data['track_list']:
        for l in k.values():
            api_lyrics = base_url+ly_param+format_url+'&track_id='+str(l['track_id'])+api_key
            ly_response = rq.get(api_lyrics)
            url.append(api_lyrics)
            new_data = ly_response.json()
            new_data = new_data['message']['body']
            for m in new_data.values():
                lyrics.append(m['lyrics_body'])     
    final_result = dict(zip(tracks, url))
    return final_result

################################################
def getLyrics(url):
    lyrics1=[]
    ly_response = rq.get(url)
    new_data = ly_response.json()
    lyric_data = new_data['message']['body']['lyrics']['lyrics_body']
#     print("Before")
#     print(lyric_data)
    lyric_data= lyric_data[:lyric_data.rfind('\n')] #eliminates last line of the lyrics
    lyric_data= lyric_data[:lyric_data.rfind('\n')] #eliminates last line of the lyrics
#     print("After")
#     print(lyric_data)
    return lyric_data

################################################

def toneAnalyzer(lyrics):
    tone_analyzer = ToneAnalyzerV3(
        version='2016-05-19',
        iam_apikey='xRTFsyatVym6NfGc64o5oLwBfVABQicz396CjHuXy5y4',
        url='https://gateway-wdc.watsonplatform.net/tone-analyzer/api'
    )

    tone_analysis = tone_analyzer.tone(
        {'text': lyrics},
        'application/json',
        sentences = 'false',
        tones = 'emotion'
    ).get_result()
    tone= json.dumps(tone_analysis, indent=2)
    # converting the string obtained from json.dumps() to json format
    dcmnt_tone_json = json.loads(tone)
    dcmnt_tone = dcmnt_tone_json['document_tone']['tone_categories']

    # retrieving the dictionary in the list obtained in dcmnt_tone
    tone_category_dict = dcmnt_tone[0]

    dict_emotion = {}
    happy_sad_dict = {}
    for val in tone_category_dict['tones']:
        dict_score_emotion = {val['tone_name']:val['score']}
        dict_emotion.update(dict_score_emotion)
        if val['tone_name'] == 'Joy' or val['tone_name'] == 'Sadness':
            happy_sad = {val['tone_name']:val['score']}
            happy_sad_dict.update(happy_sad)   
    final_tone = max(happy_sad_dict.items(), key=operator.itemgetter(1))[0]
    return final_tone

################################################      

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/result" , methods=['GET','POST'])
def result():
    if request.method =='POST':
        result = request.form
        userNum=request.form['otherText']
        coun = request.form['countries']
        num = request.form['noOfSongs']
        methods = 'POST'
        if userNum == '':
            a = 'empty'
        else:
            num = userNum
        tracks = getResponse(coun,num)
        return render_template("songslist.html",tracks = tracks,coun=coun,num=num,methods=methods)
        
    elif request.method =='GET':
        Home = request.args.get('HomeButton')
        if Home == 'Home':
            return redirect('/')
        else:
            coun = request.args.get('Country')
            num = request.args.get('Songs')
            url = request.args.get('song_val')
            methods = 'GET'
            tracks = getResponse(coun,num)
            url_value = getLyrics(url)
            lyric_tone = toneAnalyzer(url_value)
            return render_template("songslist.html",tracks=tracks,url_value = url_value,lyric_tone=lyric_tone,methods=methods,url=url,coun=coun,num=num)

if __name__ == '__main__':
    app.run(host='0.0.0.0')


# In[ ]:




