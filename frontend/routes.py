from fastapi import APIRouter, Request

from api.templates import templates

frontend_router = APIRouter()


@frontend_router.get("/app")
def app_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
        },
    )