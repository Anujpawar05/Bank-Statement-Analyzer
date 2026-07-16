import re


class DescriptionCleaner:
    """
    Cleans raw bank transaction descriptions.
    """

    REMOVE_PATTERNS = [
        r"\bAT\s+\d+\b",
        r"\bPERSONAL BANKING BR\b",
        r"\bPERSONAL BANKING\b",
        r"\bBANKING BR\b",
        r"\bBHANDARA\b",
        r"\bDEP TFR\b",
        r"\bWDL TFR\b",
        r"\bTRANSFER\b",
        r"\bREF NO\b.*",
    ]

    def clean(self, description: str) -> str:

        text = description

        for pattern in self.REMOVE_PATTERNS:
            text = re.sub(pattern, "", text, flags=re.IGNORECASE)

        text = re.sub(r"\s+", " ", text)

        return text.strip()