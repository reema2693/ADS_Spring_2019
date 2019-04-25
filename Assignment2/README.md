# Feature Engineering and Exploratory Data Analysis
*******************************************************

### Claat
https://codelabs-preview.appspot.com/?file_id=1cwr2eN0y1F-XP3N0C8Y8hvvFrrLdNRP2uc0JpqfkvZ0#0

### Before execution install below libraries
•	pandas

•	nltk

•	boto3

•	xlwt

### Dataset
•	Final_Words.csv - List of final words

•	Cluster.csv - Clusters of different banking sectors and words belonging to each cluster

### Instruction to exceute files
#### Step 1 (Part 1):

Description_Final_S3.ipynb - File to convert all the CSV files of 12 Banking Companies into a standard format with four columns i.e. Job Urls, Job Title, Description and Bank Name.

#### Step 2 (Part 2):
Formed clusters of different banking sectors and grouped some fintech words under these clusters

#### Step 3 (Part 3):

Classifier_Final_S3.ipynb - Performed feature engineering to add 3 features 
Focused Area pertaining to the technology

Banking Sector (Cluster)

Job Category (Fintech/Non-Fintech)

#### Step 4 (Part4):
Performed detailed analysis and included demographics in the claat document.

#### Step 5 (Part 5):
Creating a pipeline with airflow and dockerize the entire pipeline.

