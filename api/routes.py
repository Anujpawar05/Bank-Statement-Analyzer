from fastapi import APIRouter, File, UploadFile, Depends
from pathlib import Path
from fastapi.responses import FileResponse

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
async def analyze(
    file: UploadFile = File(...),
    service=Depends(get_processing_service),
):

    pdf_path = service.save_upload(file)

    excel_path = (
        service.upload_dir /
        f"{Path(file.filename).stem}_analysis.xlsx"
    )

    service.generate_excel(
        str(pdf_path),
        str(excel_path)
    )

    return FileResponse(
        path=str(excel_path),
        filename=excel_path.name,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )