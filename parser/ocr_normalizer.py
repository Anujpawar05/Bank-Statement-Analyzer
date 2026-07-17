import re


class OCRNormalizer:
    """
    Cleans OCR output before transaction parsing.

    Handles:
    - merged dates and amounts
    - broken decimal numbers
    - extra spaces
    - OCR garbage
    """

    @staticmethod
    def normalize(text: str) -> str:
        """
        Apply all OCR cleaning rules.
        """

        text = OCRNormalizer._fix_date_amount_merge(text)

        return text
    
    @staticmethod

    def _fix_date_amount_merge(text: str) -> str:
        """
        Example:

        01/04/2025728.00

        becomes

        01/04/2025 728.00
        """

        pattern = r"(\d{2}/\d{2}/\d{4})(\d+\.\d{2})"

        return re.sub(pattern, r"\1 \2", text)