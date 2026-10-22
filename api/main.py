import sys
import threading
from fastapi import FastAPI
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

import os
from pathlib import Path
from api.routes import router
from frontend.routes import frontend_router

BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="Bank Statement Analyzer API",
    version="1.0.0",
    description="REST API for Bank Statement Analyzer",
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