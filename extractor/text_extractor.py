import fitz


class TextExtractor:
    """
    Extracts embedded text from a PDF document.
    """

    def extract(self, document: fitz.Document) -> str:
        """
        Extract all text from every page in the PDF.

        Args:
            document: An opened PyMuPDF document.

        Returns:
            A single string containing all extracted text.
        """

        extracted_text = []

        for page in document:
            page_text = page.get_text()

            if page_text:
                extracted_text.append(page_text)

        return "\n".join(extracted_text)