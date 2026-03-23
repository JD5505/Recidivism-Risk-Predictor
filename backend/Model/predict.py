import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))

def predict_proba(input_dict : dict):
    input_df = pd.DataFrame([input_dict])

    prediction = model.predict_proba(input_df)[0][1]
    return prediction