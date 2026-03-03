from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.user_input import UserInput
from Model.predict import predict_proba
app = FastAPI()

@app.get('/')
def home():
    return {'Message': 'Welcome to the Recidivism risk prediction API'}

@app.post('/predict')
def userinput(data: UserInput):
    input_dict = {
        'age' : data.age,
        'juv_fel_count': data.juv_fel_count,
        'juv_misd_count' : data.juv_misd_count,
        'juv_other_count' : data.juv_other_count,
        'priors_count' : data.priors_count,
        'c_charge_degree' : data.c_charge_degree,
        'c_days_from_compas' : data.c_days_from_compas,
        'age_cat' : data.age_cat
    }

    output = predict_proba(input_dict)
    if output >= 0.50:
        output = 1
    else:
        output = 0
    
    return JSONResponse(status_code=200, content={'prediction': output})