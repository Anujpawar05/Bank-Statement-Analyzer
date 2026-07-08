"""
ocr_extractor.py

Extract text from images using PaddleOCR.
"""

import os
from pathlib import Path

# Disable oneDNN (MKLDNN) before importing PaddleOCR
os.environ["FLAGS_use_mkldnn"] = "0"

from paddleocr import PaddleOCR


class OCRExtractor:
    """
    Extract text from one or more images using PaddleOCR.
    """

    def __init__(self):
        # English only for Version 1
        self.ocr = PaddleOCR(
            lang="en",
            use_doc_orientation_classify=False,
            use_doc_unwarping=False,
            use_textline_orientation=False,
        )

    def extract(self, image_paths) -> str:
        """
        Perform OCR on a list of image files.

        Parameters
        ----------
        image_paths : list[pathlib.Path]

        Returns
        -------
        str
        """

        extracted_pages = []

        for image_path in image_paths:

            result = self.ocr.predict(str(image_path))

            page_lines = []

            for page in result:

                if "rec_texts" in page:
                    page_lines.extend(page["rec_texts"])

            extracted_pages.append("\n".join(page_lines))

        return "\n\n".join(extracted_pages)