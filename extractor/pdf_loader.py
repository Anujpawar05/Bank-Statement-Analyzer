from pathlib import Path

import fitz


class PDFLoader:
   

    def __init__(self, pdf_path: Path):
        self.pdf_path = Path(pdf_path)

    def load(self, password: str | None = None) -> fitz.Document:
       

        if not self.pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found: {self.pdf_path}"
            )

        document = fitz.open(self.pdf_path)

        if document.needs_pass:
            if not password or not str(password).strip():
                raise ValueError(
                    "This PDF is password protected."
                )

            clean_pw = str(password).strip()
            if not document.authenticate(clean_pw):
                raise ValueError(
                    "Incorrect PDF password."
                )

        return document