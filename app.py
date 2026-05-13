from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
import json
import pickle
import pandas as pd
from predict import predict_output, MODEL_VERSION 
from schema.predicted_response import PredictionResponse


app=FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Category Predictor API!"}


@app.get("/health")
def health_check():
    return {
        "status": "API is healthy and running!",
        "model_version": MODEL_VERSION,
        "Model_loaded": model is not None
        }    

@app.post("/predict",response_model=PredictionResponse) 
def predict_premium(data : UserInput):

    user_input = {
        "bmi" : data.bmi,
        "age_group": data.age_group,
        "lifestyle_risk": data.lifestyle_risk,
        "city_tier": data.city_tier,
        "income_lpa": data.income_lpa,
        "occupation": data.occupation
    }
    try:
        prediction = predict_output(user_input) 
    
        return JSONResponse(status_code=200,content={"response": prediction})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))  



    

 
