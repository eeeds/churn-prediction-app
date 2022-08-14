

# Import dependencies
import pandas as pd

import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline



input_data = './datasets/Churn_Modelling.csv'
output_model = './models/pipeline.bin'

print(f'Reading data from {input_data}...')
df = pd.read_csv(input_data)
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis = 1)


categorical = ['Geography', 'Gender']
numerical = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary']

##Divide the df into df_train and df_test
df_train_all, df_test = train_test_split(df, test_size = 0.3, random_state = 0)


##Training model 
df_train, df_val = train_test_split(df_train_all, test_size = 0.3, random_state = 0)


y_train = df_train.Exited.astype(int).values
y_val = df_val.Exited.astype(int).values

##Use Dict Vectorizer to transform categorical variables into numerical variables
train_dicts = df_train[categorical + numerical].to_dict(orient = 'records')
val_dicts = df_val[categorical + numerical].to_dict(orient = 'records')


## Let's make the pipeline

Pipeline = make_pipeline(
    DictVectorizer(),
    RandomForestClassifier(n_estimators = 100, random_state = 0)
)

Pipeline.fit(train_dicts, y_train)


## Test our Pipeline
y_pred = Pipeline.predict_proba(val_dicts)[:,1]

## Evaluate the model
auc = roc_auc_score(y_val, y_pred)

print(f'AUC value: {auc:0.3f}')

print(f'Saving model into {output_model}...')

with open (output_model, 'wb' ) as f_out: 
    pickle.dump(Pipeline, f_out)



