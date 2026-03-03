import pandas as pd
import joblib

model = joblib.load('Model/model.pkl')

def predict_proba(input_dict : dict):
    input_df = pd.DataFrame([input_dict])

    prediction = model.predict_proba(input_df)[0][1]
    return prediction