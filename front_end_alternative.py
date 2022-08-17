import pickle
import gradio as gr

def load_model():
    model = 'models/pipeline.bin'

    with open(model, 'rb') as f_in:
        pipeline = pickle.load(f_in)

    return pipeline

pipeline = load_model()

def variables(credit_score,  geography, gender, age, tenure, balance, num_of_products, has_cr_card,
is_active_member, estimated_salary):
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
    return pipeline.predict_proba(customer)[0,1]

block = gr.Interface(
    fn = variables,
    inputs = [gr.Slider(0,1000),gr.Radio(['France', 'Spain', 'Germany']),gr.Radio(['Male', 'Female']) ,gr.Slider(0,100), gr.Slider(0,10), gr.Slider(0,300000), 
    gr.Slider(0,10), gr.Checkbox(['Yes', 'NO']), gr.Checkbox(['Yes', 'NO']), gr.Slider(0,1000000)],
    outputs = ["number"]
)
block.launch()