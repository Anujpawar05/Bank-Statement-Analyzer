import re


class MetadataExtractor:
    """
    Extracts statement metadata from raw bank statement text.
    """

    def extract(self, text: str) -> dict:
        return {
            "bank_name": self._extract_bank_name(text),
            "account_holder": self._extract_account_holder(text),
            "account_number": self._extract_account_number(text),
            "ifsc": self._extract_ifsc(text),
            "branch": self._extract_branch(text),
            "statement_period": self._extract_statement_period(text),
        }

    def _extract_bank_name(self, text: str):
        if "State Bank of India" in text:
            return "State Bank of India"

        first_line = text.splitlines()[0].strip()

        return first_line

    def _extract_account_holder(self, text: str):
        lines = text.splitlines()

        for line in lines:
            line = line.strip()

            if line.startswith("Mr.") or line.startswith("Mrs.") or line.startswith("Ms."):
                return line

        match = re.search(
            r"Account\s*Name\s*:?\s*(.+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""

    def _extract_account_number(self, text: str):
        match = re.search(
            r"Account\s*Number\s*:?\s*([0-9]{9,20})",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1)

        return ""

    def _extract_ifsc(self, text: str):
        match = re.search(
            r"IFSC(?:\s*Code)?\s*:?\s*([A-Z]{4}0[A-Z0-9]{6})",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1)

        return ""

    def _extract_branch(self, text: str):
        match = re.search(
            r"Branch\s*Name\s*:?\s*(.+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        match = re.search(
            r"Branch\s*:?\s*(.+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""

    def _extract_statement_period(self, text: str):
        match = re.search(
            r"Statement\s*From\s*:?\s*([0-9/\-]+\s*to\s*[0-9/\-]+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1)

        match = re.search(
            r"Statement\s*Period\s*:?\s*(.+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""