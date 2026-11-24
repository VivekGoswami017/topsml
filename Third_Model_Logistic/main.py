
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib

app = FastAPI()

# Enable CORS for React frontend (allows requests from any port/origin)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        "predicted_Result": round(float(Result[0]), 2),
        "status": "Pass" if int(Result[0]) == 1 else "Fail"
    }
