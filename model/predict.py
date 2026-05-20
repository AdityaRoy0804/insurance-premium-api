import joblib
import pandas as pd

# load the trained model
model_path = "model/insurance_premium_model.pkl"
with open(model_path, "rb") as f:
    model = joblib.load(f)

# get classes from the model(for confidence score)
class_labels = model.classes_.tolist()

# function to make predictions
def predict_insurance_premium(input_data: dict):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    predicted_premium = model.predict(input_df)[0]
    
    # Get confidence scores for each class
    confidence_scores = model.predict_proba(input_df)[0]
    
    # Create a dictionary of class labels and their corresponding confidence scores
    confidence_dict = {class_labels[i]: confidence_scores[i] for i in range(len(class_labels))}
    
    return {
        "predicted_premium": predicted_premium,
        "confidence_scores": confidence_dict
    } 