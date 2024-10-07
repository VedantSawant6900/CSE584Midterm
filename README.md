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
├── HyperParameterTestClassifier.ipynb - This the Deep Learning Classifier which uses BERT model with different Parameters than that of the best one.
├── Miscellaneous - These are the Miscellaneous scripts and files which were created during the course of project
├── README.md
├── Vedant_Sawant_Midterm_Report.pdf - This the Project report
├── dataset.csv - This contains the whole dataset on which model was trained.
└── requirements.txt - This is the requirements file which needs to be installed before executing the project.
├── bloom.ipynb - This file is used to create the xij for bloom model.
├── gptj.ipynb - This file is used to create the xij for gptj model.
├── llama.ipynb - This file is used to create the xij for llama model.
├── opt.ipynb - This file is used to create the xij for opt model.
├── pythia.ipynb - This file is used to create the xij for pythia model.
└── xi.txt - Collection of xi


````
## Program Code execution
### Classifier
I have already created the dataset.csv file. So if you want to replicate the results of the deep learning classifier, then run the cells of Classifier notebook
````
├── DeepLearningBertClassifier.ipynb. - This is the best Deep Learning Classifier which uses BERT model and gave accuracy of 40%
├── DeepLearningClassifier.ipynb - This is the Deep Learning LSTM RNN Classifier that i created from scrat which gave 26% validation accuracy
├── HyperParameterTest.ipynb - This the Deep Learning Classifier which uses BERT model with different Parameters than that of the best one.

````
### Creating Dataset
I have added xi.txt file which contains all the xi. So if you want to create a dataset of a particular model then run the cells of the <model_name>.ipynb file.
````
├── bloom.ipynb - This file is used to create the xij for bloom model.
├── gptj.ipynb - This file is used to create the xij for gptj model.
├── llama.ipynb - This file is used to create the xij for llama model.
├── opt.ipynb - This file is used to create the xij for opt model.
├── pythia.ipynb - This file is used to create the xij for pythia model.
└── xi.txt - Collection of xi
````
This will create a xij<model_name>.txt. Then use the entries of these txt and then create a dataset.csv. 
Dataset.csv has 2 columns where one is completed xij named 'x' and other is the label of the model used named 'y'.