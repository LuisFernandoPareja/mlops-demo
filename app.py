from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load("model/model.pkl")

# Define input data structure using Pydantic
class Features(BaseModel):
    data: list  # expects a list of 4 float features

# Root endpoint
@app.get("/")
def root():
    return {"message": "Model is running!"}

# Prediction endpoint
@app.post("/predict")
def predict(features: Features):
    # Convert list to numpy array and predict
    prediction = model.predict([np.array(features.data)])
    return {"prediction": prediction.tolist()}
