from pathlib import Path
import shutil

from fastapi import UploadFile
from exporter.workbook_generator import WorkbookGenerator
from pipeline.processing_pipeline import ProcessingPipeline


class ProcessingService:
    """
    Service layer responsible for processing bank statements.
    """

    def __init__(self):
        self.pipeline = ProcessingPipeline()

        self.upload_dir = Path("uploads")
        self.upload_dir.mkdir(exist_ok=True)
        self.workbook_generator = WorkbookGenerator()

    def save_upload(self, file: UploadFile) -> Path:
        """
        Save uploaded PDF to uploads folder.
        """

        destination = self.upload_dir / file.filename

        with destination.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return destination

    def process_pdf(self, pdf_path: str) -> dict:
        """
        Process a PDF statement.
        """

        return self.pipeline.process(pdf_path)
    def generate_excel(self, pdf_path: str, output_path: str):

        result = self.pipeline.process(pdf_path)

        workbook = self.workbook_generator.generate(result)

        workbook.save(output_path)

        return output_path