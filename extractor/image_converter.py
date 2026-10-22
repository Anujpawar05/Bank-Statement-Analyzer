"""
image_converter.py

Converts PDF pages into PNG images.
"""

import os
import tempfile
from pathlib import Path

import fitz


class ImageConverter:
    """
    Convert PDF pages into images.
    """

    def convert(self, document: fitz.Document, output_dir: str = "temp"):
        """
        Convert every page of a PDF into a PNG image.

        Parameters
        ----------
        document : fitz.Document
            Opened PDF document.

        output_dir : str
            Folder where images will be saved.

        Returns
        -------
        list[Path]
            List of generated image paths.
        """

        if output_dir == "temp" and (os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME")):
            output_path = Path(tempfile.gettempdir()) / "temp"
        else:
            output_path = Path(output_dir)

        output_path.mkdir(parents=True, exist_ok=True)

        image_paths = []

        for page_number, page in enumerate(document, start=1):

            pixmap = page.get_pixmap(dpi=120)

            image_file = output_path / f"page_{page_number}.png"

            pixmap.save(image_file)

            image_paths.append(image_file)

        return image_paths