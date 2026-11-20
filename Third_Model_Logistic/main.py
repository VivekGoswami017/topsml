
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

# Load ML Model
model = joblib.load("Logistic_model.pkl")


class DataScience(BaseModel):
    StudyHours: float


@app.get("/")
def test():
    return {"msg": "Uvicorn is running"}


@app.post("/predict")
def datainsert(ds: DataScience):

    Result = model.predict([[ds.StudyHours]])

    return {
        "predicted_Result": round(float(Result[0]), 2)
    }
