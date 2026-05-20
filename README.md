# Insurance Premium Prediction System

A machine learning powered web application that predicts insurance premium categories using FastAPI, Scikit-learn, and a modern HTML/CSS/JavaScript frontend.

---

## Features

- Insurance premium category prediction
- Confidence score visualization
- FastAPI REST API backend
- Interactive frontend with JavaScript fetch API
- Real-time predictions without page reload
- Responsive UI with gradient-based design
- Input validation using Pydantic
- ML pipeline with preprocessing and feature engineering

---

## Tech Stack

### Backend
- FastAPI
- Scikit-learn
- Pydantic
- Uvicorn

### Frontend
- HTML
- CSS
- JavaScript

### Machine Learning
- Pandas
- NumPy
- Joblib

---

## Project Structure

```bash
InsuranceAPI_Project/
│
├── api.py
├── requirements.txt
├── README.md
│
├── model/
│   ├── predict.py
│   └── insurance_premium_model.pkl
│
├── schema/
│   └── input_validation.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── notebook/
    └── model_training.ipynb