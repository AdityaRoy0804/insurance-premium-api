## Streamlit based UI for checking the model & API functionality

import streamlit as st
import requests

# Set the API endpoint
API_URL = "http://localhost:8000/predict"

# Streamlit app

st.title("Insurance Premium Prediction")
st.markdown("Enter the details of the person to predict the insurance premium.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120, value=30)
weight = st.number_input("Weight (kg)", min_value=0.1, value=70.0)
height = st.number_input("Height (m)", min_value=0.1, max_value=2.5, value=1.75)
income_lpa = st.number_input("Income (LPA)", min_value=0.1, value=5.0)
smoker = st.selectbox("Smoker", options=[True, False])
city = st.text_input("City", value="Mumbai")
occupation = st.selectbox("Occupation", options=['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])

# Prediction Logic
if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation
    }
    
    try:
        response = requests.post(API_URL, json=input_data) # post request to the API with input data
        result = response.json()
        
        if response.status_code == 200 and "response" in result:
            # in response it will have predicted_premium and confidence_scores
            predicted_premium = result["response"]["predicted_premium"] 
            confidence_scores = result["response"]["confidence_scores"]
            st.success(f"Predicted Premium Category: {predicted_premium}")
            st.subheader("Confidence Scores:")
            for category, score in confidence_scores.items():
                st.write(f"{category}: {score:.2f}")
        else:
            st.error(f"Error: {result.get('error', 'Unknown error occurred')}")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        

            
        