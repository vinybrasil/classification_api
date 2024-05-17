from fastapi import FastAPI

from app.handlers import prediction_pipeline
from app.schemas import RequestSchema, ResponseSchema

app = FastAPI()


@app.get("/api/v1/health")
async def health_check():
    return {"status": "alive"}


@app.post("/api/v1/predict")
async def handle_data(request: RequestSchema):
    response: ResponseSchema = prediction_pipeline(request)
    return response
