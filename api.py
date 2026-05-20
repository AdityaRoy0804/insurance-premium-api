from fastapi import FastAPI
from fastapi.responses import JSONResponse
from model.predict import predict_insurance_premium, load_model_check
from schema.input_validation import user_input

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the Insurance Premium Prediction API !!"}

@app.get("/health")
def health_check():
    model_status = load_model_check()
    return {
        "status": "OK",
        "model_status": model_status
    }



