from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api.routes import router
from frontend.routes import frontend_router

app = FastAPI(
    title="Bank Statement Analyzer API",
    version="1.0.0",
    description="REST API for Bank Statement Analyzer",
)

app.include_router(router)
app.include_router(frontend_router)

app.mount(
    "/static",
    StaticFiles(directory="frontend/static"),
    name="static",
)