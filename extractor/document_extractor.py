"""
document_extractor.py

Coordinates the document extraction pipeline.

Workflow:
1. Try extracting embedded text.
2. If text exists, return it.
3. Otherwise, OCR will be used (implemented in the next sprint).
"""

from extractor.text_extractor import TextExtractor


class DocumentExtractor:
    """
    Coordinates document text extraction.

    This class acts as the single entry point for obtaining text
    from a document.
    """

    def __init__(self):
        self.text_extractor = TextExtractor()

    def extract(self, document) -> str:
        """
        Extract text from the document.

        Parameters
        ----------
        document : fitz.Document

        Returns
        -------
        str
            Extracted text.
        """

        text = self.text_extractor.extract(document)

        if text.strip():
            return text

        # OCR fallback will be added in Sprint 5
        return ""