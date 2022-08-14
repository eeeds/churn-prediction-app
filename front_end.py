import streamlit as st
from PIL import  Image


st.write("""
# Churn-Prediction-App
This app predicts if a customer will leave the bank or not.
"""
)
image = Image.open('images/churn-fish.webp')
st.image(image, caption='')

gender = st.selectbox(
    'Gender',
    ('Male', 'Female')
)


geography = st.selectbox(
    'Geography',
    ('Spain', 'France', 'Germany')
)

age = st.slider(
    'Age',
    min_value = 18,
    max_value = 100,
    value = 35
)

has_cr_card = st.selectbox(
    'HasCrCard',
    ('Yes', 'NO')
)
credit_score = st.slider(
    'CreditScore',
    min_value = 350,
    max_value = 850,
    value = 500
)

tenure = st.slider(
    'Tenure',
    min_value = 0,
    max_value = 10,
    value = 5
)

balance = st.slider(
    'Balance',
    min_value = 0,
    max_value = 300000,
    value = 150000
)

num_of_products = st.slider(
    'NumOfProducts',
    min_value = 0,
    max_value = 30,
    value = 2
)

estimated_salary = st.slider(
    'EstimatedSalary',
    min_value = 0,
    max_value = 200000,
    value = 50000
)

is_active_member = st.selectbox(
    'IsActiveMember',
    ('Yes', 'No')

)

# customer = {
#     ''
# }

st.write("""
This project was done as a part of [the project-of-the-week 
initiative at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-08-14-frontend.md).
""")