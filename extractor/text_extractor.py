import fitz


class TextExtractor:
    """
    Extract embedded text from a PDF document.
    """

    def extract(self, document: fitz.Document) -> str:
        """
        Extract text from all pages.

        Parameters
        ----------
        document : fitz.Document

        Returns
        -------
        str
        """

        pages = []

        for page_number, page in enumerate(document, start=1):

            text = page.get_text("text")

            if text.strip():
                pages.append(text)

        return "\n".join(pages)