"""
Bank Detector

Detects which bank issued the statement by looking
for unique keywords in the extracted text.
"""


class BankDetector:
    """
    Detect the bank from extracted statement text.
    """

    # Keywords used to identify supported banks.
    BANK_KEYWORDS = {
        "SBI": [
            "STATE BANK OF INDIA",
            "SBI",
        ],
        "BOB": [
            "BANK OF BARODA",
        ],
        "HDFC": [
            "HDFC BANK",
            "HDFC BANK LTD",
        ],
    }

    def detect(self, text: str) -> str:
        """
        Detect the bank name from statement text.

        Parameters
        ----------
        text : str
            Extracted statement text.

        Returns
        -------
        str
            Bank code if detected, otherwise 'UNKNOWN'.
        """

        if not text:
            return "UNKNOWN"

        text = text.upper()

        for bank, keywords in self.BANK_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text:
                    return bank

        return "UNKNOWN"