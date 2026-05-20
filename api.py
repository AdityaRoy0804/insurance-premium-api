from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from model.predict import predict_insurance_premium, load_model_check
from schema.input_validation import user_input

app = FastAPI()

# Allow CORS for respective origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5501", "http://localhost:5501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Endpoints and Routes

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

@app.post("/predict")
def predict_premium(user_data: user_input):
    input_dict = user_data.model_dump()
    try:
        prediction_result = predict_insurance_premium(input_dict)
        return JSONResponse(status_code=200, content={"response": prediction_result})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
    

