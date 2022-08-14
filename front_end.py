from contextlib import suppress
import streamlit as st
from PIL import  Image
import pickle 
import json 

st.write("""
# Churn-Prediction-App
This app predicts if a customer will leave the bank or not.
"""
)
st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

@st.cache(suppress_st_warning=True, allow_output_mutation=True)
def load_model():
    model = 'models/pipeline.bin'

    with open(model, 'rb') as f_in:
        pipeline = pickle.load(f_in)

    return pipeline

pipeline = load_model()


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

customer = {'CreditScore': float(credit_score),
 'Geography': str(geography),
 'Gender': str(gender),
 'Age': int(age),
 'Tenure': int(tenure),
 'Balance': float(balance),
 'NumOfProducts': int(num_of_products),
 'HasCrCard': str(has_cr_card)=='Yes',
 'IsActiveMember': str(is_active_member)=='Yes',
 'EstimatedSalary': float(estimated_salary),
 }
pred = pipeline.predict_proba(customer)[0,1]
pred = float(pred)
col1_pred, col2_pred = st.columns(2)

col1_pred.write("Probability of acceptance:")
col2_pred.write(f"{pred*100:.2f}%")


st.write("""
This project was done as a part of [the project-of-the-week 
initiative at DataTalks.Club](https://github.com/DataTalksClub/project-of-the-week/blob/main/2022-08-14-frontend.md).
""")