import requests
import json 

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

r = requests.post(URL, json=REQUEST)
print(r.json())