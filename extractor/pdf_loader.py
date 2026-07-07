from pathlib import Path

import fitz


class PDFLoader:
    """
    Opens and validates PDF documents.

    Responsibilities:
    - Verify file exists
    - Open PDF
    - Handle password-protected PDFs
    - Return a PyMuPDF document object
    """

    def __init__(self, pdf_path: Path):
        self.pdf_path = Path(pdf_path)

    def load(self, password: str | None = None) -> fitz.Document:
        """
        Open a PDF document.

        Args:
            password: Password for encrypted PDFs (optional).

        Returns:
            fitz.Document

        Raises:
            FileNotFoundError
            ValueError
        """

        if not self.pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found: {self.pdf_path}"
            )

        document = fitz.open(self.pdf_path)

        if document.needs_pass:

            if password is None:
                raise ValueError(
                    "This PDF is password protected."
                )

            if not document.authenticate(password):
                raise ValueError(
                    "Incorrect PDF password."
                )

        return document