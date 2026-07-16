from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse
import tempfile
import os
import shutil

from api.dependencies import get_processing_service

router = APIRouter()


@router.get("/")
def root():
    return {
        "project": "Bank Statement Analyzer",
        "status": "Running",
        "version": "1.0.0",
    }


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    upload_dir = tempfile.mkdtemp()

    pdf_path = os.path.join(upload_dir, file.filename)

    with open(pdf_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    excel_path = os.path.join(upload_dir, "analysis.xlsx")

    service = get_processing_service()

    service.generate_excel(
        pdf_path=pdf_path,
        output_path=excel_path,
    )

    return FileResponse(
        path=excel_path,
        filename="analysis.xlsx",
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )