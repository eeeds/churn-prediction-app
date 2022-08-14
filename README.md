# Churn-prediction app.

This project has been created to predict the churn of a customer and it's part of a challenge called [Project-of-the-week](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-08-14-frontend.md) that is being held by [Datatalks.club](https://datatalks.club/slack.html).
# Content
- [Churn-prediction app.](#churn-prediction-app)
- [Content](#content)
- [Tools](#tools)
- [Dataset](#dataset)
- [Enviroment](#enviroment)
  - [Create the enviroment](#create-the-enviroment)
  - [Activate the enviroment](#activate-the-enviroment)
  - [Install dependencies](#install-dependencies)
- [Working on the notebook](#working-on-the-notebook)
  - [Analysis conclusions](#analysis-conclusions)
  - [Jupyter Notebook into python code](#jupyter-notebook-into-python-code)
- [Flask Application](#flask-application)
  - [Create the app](#create-the-app)
  - [Run the app](#run-the-app)
  - [Send a request](#send-a-request)
- [Front end](#front-end)
  - [Install Streamlit](#install-streamlit)
  - [Working on design](#working-on-design)
  - [Run the app](#run-the-app-1)
# Tools
-   [Python](https://www.python.org/)
-   [Anaconda](https://www.anaconda.com/products/distribution)
-   [Pandas](https://pandas.pydata.org/)
-   [Scikit-learn](https://scikit-learn.org/stable/)

# Dataset
[Dataset's link](https://www.kaggle.com/datasets/shivan118/churn-modeling-dataset)

# Enviroment
I'm going to use a conda enviroment for this project called `churn-project`.
## Create the enviroment
```
conda create -n churn-project python=3.9
```
## Activate the enviroment
```
conda activate churn-project
```
## Install dependencies
```
pip install -r requirements.txt
```
# Working on the notebook
[Working on notebook: exploratory_analysis.ipynb](notebooks/exploratory_analysis.ipynb)
Follow the notebook to see the results.
## Analysis conclusions
I tested three models:
- Logistic Regression
- Random Forest
- XGBoost

| Values | Model               | Precision | Recall | f1-score |
|--------|---------------------|-----------|--------|----------|
| 0      | Logistic Regression | 0.83      | 0.96   | 0.89     |
| 1      | Logistic Regression | 0.61      | 0.22   | 0.32     |
| 0      | Random Forest       | 0.88      | 0.96   | 0.92     |
| 1      | Random Forest       | 0.77      | 0.50   | 0.61     |
| 0      | XGBoost             | 0.89      | 0.95   | 0.91     |
| 1      | XGBoost             | 0.72      | 0.53   | 0.61     |

**Random Forest** and **XGBoost** have performed better than **Logistic Regression** and they have the same f1-score.

## Jupyter Notebook into python code 
You can transform your notebook into python code by using the command:
```
jupyter nbconvert --to python exploratory_analysis.ipynb
```
# Flask Application
Install Flask with the command:
```
pip install flask
```
## Create the app
[Working on serve.py](serve.py)
## Run the app
```
python serve.py
```
## Send a request
I've created a simple script called `serve_test.py` that sends a request to the app and prints the response
with this values:
```
REQUEST={
  "CreditScore": 597,
  "Geography": "Germany",
  "Gender": "Female",
  "Age": 35,
  "Tenure": 8,
  "Balance": 131101.04,
  "NumOfProducts": 1,
  "HasCrCard": 1,
  "IsActiveMember": 1,
  "EstimatedSalary": 192852.67,
  "Exited": 0
}

URL='http://localhost:9696/predict'
```

# Front end
I'm going to use a [Streamlit.io](https://streamlit.io/) front end for this project.

## Install Streamlit
```
pip install streamlit
```
## Working on design
Working on front in [Front End](front_end.py)
## Run the app
```
streamlit run front_end.py
```