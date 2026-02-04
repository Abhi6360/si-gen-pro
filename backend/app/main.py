
from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="SI-GEN Pro API")
app.include_router(router)
