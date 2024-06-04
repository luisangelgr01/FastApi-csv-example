from fastapi import FastAPI
from endpoints.csv_endpoint import router as csv_router

app = FastAPI()

app.include_router(csv_router, prefix="/api/v1")