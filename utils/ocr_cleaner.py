import re


class OCRCleaner:
    """
    Cleans OCR text before parsing.
    Does NOT modify transaction meaning.
    Only fixes common OCR artifacts.
    """

    def clean(self, text: str) -> str:

        if not text:
            return ""

        # normalize line endings
        text = text.replace("\r", "\n")

        # remove repeated spaces
        text = re.sub(r"[ \t]+", " ", text)

        # remove spaces before commas/periods
        text = re.sub(r"\s+,", ",", text)
        text = re.sub(r"\s+\.", ".", text)

        # collapse multiple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text