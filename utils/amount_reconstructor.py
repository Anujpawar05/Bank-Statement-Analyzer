import re


class AmountReconstructor:
    """
    Repairs OCR-merged monetary values.
    """

    MONEY_PATTERN = re.compile(r"\d+\.\d{2}")

    def split(self, text: str) -> list[str]:
        """
        Extract all monetary values from a merged OCR string.

        Example:
            228.06843.30

        Returns:
            ["228.06", "843.30"]
        """

        return self.MONEY_PATTERN.findall(text)