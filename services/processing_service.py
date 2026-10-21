import time
from pathlib import Path
import shutil
from pipeline.processing_pipeline import ProcessingPipeline
from exporter.workbook_generator import WorkbookGenerator


class ProcessingService:

    def __init__(self):
        self.pipeline = ProcessingPipeline()
        self.workbook_generator = WorkbookGenerator()

        self.upload_dir = Path("uploads")
        self.upload_dir.mkdir(exist_ok=True)

    def save_upload(self, file):
        pdf_path = self.upload_dir / file.filename

        with open(pdf_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return pdf_path

    def generate_excel(
        self,
        pdf_path,
        excel_path,
        password=None
    ):

        total_start = time.time()

        print("=" * 60)
        print("Starting Processing")
        print("=" * 60)

        step = time.time()

        result = self.pipeline.process(
            pdf_path,
            password=password
        )

        print(f"Pipeline completed in {time.time() - step:.2f} seconds")

        step = time.time()

        workbook = self.workbook_generator.generate(result)

        print(f"Workbook generated in {time.time() - step:.2f} seconds")

        step = time.time()

        workbook.save(excel_path)

        print(f"Workbook saved in {time.time() - step:.2f} seconds")

        print("=" * 60)
        print(f"TOTAL TIME: {time.time() - total_start:.2f} seconds")
        print("=" * 60)

        return result