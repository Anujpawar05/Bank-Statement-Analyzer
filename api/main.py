from fastapi import FastAPI
from api.routes import router

app = FastAPI(
    title="Bank Statement Analyzer API",
    version="1.0.0",
    description="REST API for Bank Statement Analyzer",
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "project": "Bank Statement Analyzer",
        "status": "running",
        "version": "1.0.0",
    }