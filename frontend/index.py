import streamlit as st
import requests

API_URL = 'https://recidivism-risk-predictor.onrender.com/predict'

st.set_page_config(
    page_title="Recidivism Risk Predictor",
    page_icon="⚖️",
    layout="wide"
)
st.title("⚖️ Recidivism Risk Predictor")
st.caption("Please enter information of the defendant below.")

age = st.number_input('Enter Age',min_value=0, max_value=100)
juv_fel_count = st.number_input('Number of Serious Crimes done as a Juvenile(Under 18)', min_value=0, max_value=100)
juv_misd_count = st.number_input('Number of Misdemeanors done as a Juvenile(Minor Crimes)',min_value=0, max_value=100)
juv_other_count = st.number_input('Number of Other crimes done as a Juvenile',min_value=0, max_value=100)
priors_count = st.number_input('Number of Crimes done as an Adult',min_value=0, max_value=100)
charge_degree = st.selectbox('Enter Degree of Charges', options = ['F1','F2','F3','F5','F6','F7',
                                                                   'TCX','M1','M2','MO3','CO3','CT','NI0','X'])

c_days_from_compas = st.number_input('Enter the gap between Arrest/Charge and COMPAS Evaluation(In Days)', min_value=0, max_value=100)

if st.button('Predict Output'):
    input_dict = {
        'age' : age,
        'juv_fel_count': juv_fel_count,
        'juv_misd_count' : juv_misd_count,
        'juv_other_count' : juv_other_count,
        'priors_count' : priors_count,
        'charge_degree' : charge_degree,
        'c_days_from_compas' : c_days_from_compas,
    }

    try:
        response = requests.post(API_URL, json = input_dict)
        if response.status_code == 200:
            result = response.json()
            if result['prediction'] == 1:
                st.error("The Defendant Will Reoffend")
            else:
                st.success('The Defendant will not Reoffend')
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI Server. Make sure it's running on port 8000")
       