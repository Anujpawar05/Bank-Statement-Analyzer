import os
import sys
import threading
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

from api.routes import router
from frontend.routes import frontend_router
from api.templates import templates

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="Bank Statement Analyzer API",
    version="1.0.0",
    description="REST API for Bank Statement Analyzer",
)


@app.middleware("http")
async def vercel_routing_middleware(request: Request, call_next):
    raw_path = request.scope.get("path", "/")
    vercel_path = request.query_params.get("__vercel_path")
    matched_path = request.headers.get("x-matched-path")

    if vercel_path is not None:
        request.scope["path"] = "/" + vercel_path.lstrip("/")
    elif matched_path and not matched_path.startswith("/api/index"):
        request.scope["path"] = matched_path
    elif raw_path.startswith("/api/index.py"):
        request.scope["path"] = raw_path[len("/api/index.py"):] or "/"
    elif raw_path.startswith("/api/index"):
        request.scope["path"] = raw_path[len("/api/index"):] or "/"
    elif raw_path == "/api":
        request.scope["path"] = "/"

    return await call_next(request)


@app.get("/api/index.py", include_in_schema=False)
@app.get("/api/index", include_in_schema=False)
@app.get("/api", include_in_schema=False)
def vercel_entrypoint_fallback(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request},
    )


@app.on_event("startup")
def startup_event():
    # Only attempt background warm-up in persistent server environments if OCR is desired
    if os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
        return

    def _warmup():
        try:
            from extractor.ocr_extractor import OCRExtractor
            print("[Startup] Pre-loading PaddleOCR engine in background...")
            OCRExtractor.get_ocr_instance()
            print("[Startup] PaddleOCR engine ready!")
        except Exception as e:
            print(f"[Startup] OCR warmup info: {e}")

    threading.Thread(target=_warmup, daemon=True).start()


app.include_router(router)
app.include_router(frontend_router)

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "frontend" / "static")),
    name="static",
)