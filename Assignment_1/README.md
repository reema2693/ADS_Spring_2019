# US Banks Hiring Trend Analysis
*********************************

### Claat

https://codelabs-preview.appspot.com/?file_id=1ajdwDTVPhPDPI1gvP2oY78hIv9U4URfx8tMH54uHR0Y#0

### Before execution install below libraries
•	BeautifulSoup

•	pandas

•	re

•	matplotlib

•	requests

•	urljoin

•	PyPDF2

•	nltk

•	tika

•	numpy

•	io

•	csv

•	sys

•	sklearn

•	selenium

•	xlwt

•	itertools

### Dataset
•	Words.csv - We obtained all the fintech words using four pdf files.

•	WordList.csv, Words_TR.csv & tfidf_WordList.csv: Files to select the top 100 fintech words selected by using three approaches WordCount, TextRank, and TFIDF

•	url_bbt.csv & url_state_street.csv: Job URLs for both the bank's openings.

•	word_example_BBT.csv & word_example_StateStreet.csv: Final CSV files after performing cleansing, data pre-processing on them. A data collection of Job description and word count of top 100 words in each job description for all 3 approaches.

### Instruction to exceute files
Step 1 (Part 1):

Removed stopwords and cleaned four pdf file's content. Identified top 100 keywords for fintech jobs based on values obtained from each approach.

•	PDF_Splitting.ipynb - File to split the Pdfs

•	TF_IDF.ipynb - File to obtain the term frequency of each word in Job description

•	TextRank.ipynb - File to obtain the score of each word in Job description

•	WordCount.ipynb - On the basis of occurrence of the word, obtained the count of words 

Step 2 (Part 2): 

Performed web scrapping for BB&T and StateStreet Banks, in order to get job description of the banks.

•	Getting_URL_BBT.ipynb - Obtained URLs for each job opening posted on the BB&T's website

•	Getting_URL_State_Street.ipynb - Obtained URLs for each job opening posted on the StateStreet's website

•	Final_CSV_BBT.ipynb and Final_CSV_StateStreet.ipynb - Based on three approaches used in part 1, we selected 100 words and then calculated the occurrence of those words in job descriptions for both the banks.

Step 3 (Part 3):

Using final csv generated for both the banks (word_example_BBT & word_example_SS) depicted analysis and graphics are given in the report for reference.


