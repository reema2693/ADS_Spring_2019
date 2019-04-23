#

### Claat

https://codelabs-preview.appspot.com/?file_id=1Vrbd5cK9MQdbUIx4e9UqRwFBJW385MXLqR2o86eOZNM#6


### Before execution install below libraries:

numpy
pandas
featuretools
matplotlib
TPOT
plotly
h2o
auto-sklearn

### Dataset

The dataset is shared on drive refer link below

Link : https://drive.google.com/drive/folders/1JOdt9Onh6szcAKvnCkilARc-uh4EUeyv?usp=sharing

Data folder has below mentioned csvs :
loan.csv
LCDataDictionary.xlsx (dictionary for understanding each columns)
cleaned_data
FT_data_final
FT_data
MF_Data
Note: All the output files (csv) are under Data Folder

### Instructions to execute files :
Step 1: Execute Task_2_Data_Cleaning.ipynb This will generate output cleaned_data.csv

Step 2: Execute Task_2_Feature_Eng_Feature_Tools.ipynb and Task_2_Manual_Feature_Eng.ipynb 
Refer file FT_data.csv and FT_data_final.csv for feature engineering with feature tools. 
Refer FT_data_final.csv and MF_Data.csv file for manual feature engineering.

Step 3: Execute Prediction models to calculate the MAPE value

Task_3_Regression_Model.ipynb
Task_3_Neural_Networks.ipynb
Task_3_Random_Forest.ipnyb

Step 4: Perform hyperparameter optimization by executing below files
Execute HPT_Regression.ipynb --> Generating Score for Training and Testing data for L1,L2 and Elasticnet regularization
Execute Task_4_HPT_NN.ipynb

Step 5: Execute AutoML model

Task_4_AutoML_TPOT.ipynb
Task_4_AutSKLearn.ipynb
Task_4_H2O.ipynb

Step 6: Execute Task_5_Analysis.ipynb
