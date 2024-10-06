# CSE-584: Midterm Project
## Task
Given a set of truncated texts, for each piece of text xi, such as “Yesterday I went”, ask different Large Language Models (LLMs) to complete it by appending xj =”to Costco and purchased a floor cleaner.” so you get a complete text like “Yesterday I went to Costco and purchased a floor cleaner.” from each LLM. The same xi leads to different xj. Now please build a deep learning classifier to figure out, for each input (xi, xj), which LLM was used for this pair.
## Setup Environment 
Setup Python3 environment with python version 3.8 and above.
### Install requirements
Install requirements required for running the project by executing
````
pip install -r requirements.txt
````
## Folder Structure
````
.
├── Dataset. - These contain miscellaneous files which were created while creating dataset.
├── DeepLearningBertClassifier.ipynb. - This is the best Deep Learning Classifier which uses BERT model and gave accuracy of 40%
├── DeepLearningClassifier.ipynb - This is the Deep Learning LSTM RNN Classifier that i created from scrat which gave 26% validation accuracy
├── HyperParameterTest.ipynb - This the Deep Learning Classifier which uses BERT model with different Parameters than that of the best one.
├── Miscellaneous - These are the Miscellaneous scripts and files which were created during the course of project
├── README.md
├── Vedant_Sawant_Midterm_Report.pdf - This the Project report
├── dataset.csv - This contains the whole dataset on which model was trained.
└── requirements.txt - This is the requirements file which needs to be installed before executing the project.

````