"""
document_extractor.py

Coordinates the document extraction pipeline.

Workflow:
1. Try embedded text extraction.
2. If text exists, return it.
3. Otherwise convert PDF pages to images.
4. Run OCR.
5. Return OCR text.
"""

from extractor.text_extractor import TextExtractor
from extractor.image_converter import ImageConverter
from extractor.ocr_extractor import OCRExtractor
from utils.ocr_cleaner import OCRCleaner
from utils.ocr_repair import repair_ocr_text

class DocumentExtractor:
    """
    Coordinates document text extraction.
    """

    def __init__(self):
        self.text_extractor = TextExtractor()
        self.image_converter = ImageConverter()
        self.ocr_extractor = OCRExtractor()
        self.ocr_cleaner = OCRCleaner()
        self.ocr_repair = repair_ocr_text
    def extract(self, document) -> str:
        """
        Extract text from a document.

        Parameters
        ----------
        document : fitz.Document

        Returns
        -------
        str
        """

        # Step 1: Embedded text
        text = self.text_extractor.extract(document)

        if text.strip():
            print("✓ Embedded text detected.")

            text = self.ocr_cleaner.clean(text)

            return text

        print("No embedded text found.")
        print("Running OCR...")

        # Step 2: OCR
        images = self.image_converter.convert(document)

        text = self.ocr_extractor.extract(images)
                
        text = self.ocr_cleaner.clean(text)

        text = self.ocr_repair(text)

        return text