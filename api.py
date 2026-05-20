from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_insurance_premium
from schema.input_validation import user_input

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API !!"}


