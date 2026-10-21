"""
ocr_extractor.py

Extract text from images using PaddleOCR.
"""

import os
from pathlib import Path

# Disable oneDNN (MKLDNN) and model source connectivity check before importing PaddleOCR
os.environ["FLAGS_use_mkldnn"] = "0"
os.environ["PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK"] = "True"
os.environ["DISABLE_MODEL_SOURCE_CHECK"] = "True"


class OCRExtractor:
    """
    Extract text from one or more images using PaddleOCR.
    """
    _shared_ocr = None

    @classmethod
    def get_ocr_instance(cls):
        if cls._shared_ocr is None:
            from paddleocr import PaddleOCR
            cls._shared_ocr = PaddleOCR(
                lang="en",
                ocr_version="PP-OCRv4",
                use_doc_orientation_classify=False,
                use_doc_unwarping=False,
                use_textline_orientation=False,
            )
        return cls._shared_ocr

    @property
    def ocr(self):
        return self.get_ocr_instance()

    def warmup(self):
        """Warm up OCR instance."""
        _ = self.ocr

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