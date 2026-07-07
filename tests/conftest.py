from pathlib import Path

import pytest

from extractor.pdf_loader import PDFLoader


@pytest.fixture
def sample_pdf():
    """
    Returns an opened sample PDF.
    """

    pdf_path = Path("sample_data/statement.pdf")

    loader = PDFLoader(pdf_path)

    document = loader.load()

    yield document

    document.close()