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
- [Working on the project](#working-on-the-project)
  - [Conclusions](#conclusions)
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
# Working on the project
[Working on notebook: exploratory_analysis.ipynb](notebooks/exploratory_analysis.ipynb)
Follow the notebook to see the results.
## Conclusions
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