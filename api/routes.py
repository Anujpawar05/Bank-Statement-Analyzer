from fastapi import APIRouter, File, UploadFile, Depends
from pathlib import Path
from fastapi.responses import FileResponse, RedirectResponse
from fastapi import Request
from api.dependencies import get_processing_service
from fastapi import Form

router = APIRouter()


@router.get("/")
def root():
    return RedirectResponse(url="/app")


@router.get("/status")
def status_check():
    return {
        "project": "Bank Statement Analyzer",
        "status": "Running",
        "version": "1.0.0",
    }


@router.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    service=Depends(get_processing_service),
    password: str = Form(None)
):

    pdf_path = service.save_upload(file)

    excel_path = (
        service.upload_dir /
        f"{Path(file.filename).stem}_analysis.xlsx"
    )

    print("Password received:", password)

    try:

        result = service.generate_excel(
            str(pdf_path),
            str(excel_path),
            password=password
        )

    except ValueError as e:

        message = str(e).lower()

        if "password protected" in message:

            return {
                "requires_password": True,
                "message": "This PDF is password protected. Please enter the password."
            }

        if "incorrect pdf password" in message:

            return {
                "requires_password": True,
                "message": "Incorrect password. Please try again."
            }

        raise

    except RuntimeError as e:

        return {
            "error": True,
            "message": str(e)
        }

    filename = Path(excel_path).name
    transactions = result.get("transactions", [])

    nature_counts = {
        "online": sum(1 for tx in transactions if tx.get("nature") == "Online"),
        "cash": sum(1 for tx in transactions if tx.get("nature") == "Cash"),
        "card": sum(1 for tx in transactions if tx.get("nature") == "Card"),
    }

    audit = result.get("audit_report", {})
    failed_count = audit.get("failed", 0)
    is_balanced = failed_count == 0

    return {
        "metadata": result["metadata"],
        "analysis": result["analysis"],
        "transaction_count": len(transactions),
        "nature_counts": nature_counts,
        "is_balanced": is_balanced,
        "balanced_count": audit.get("passed", len(transactions)),
        "download_url": f"/download/{filename}"
    }

@router.get("/download/{filename}")
def download_file(
    filename: str,
    service=Depends(get_processing_service),
):

    file_path = service.upload_dir / filename

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )

    




