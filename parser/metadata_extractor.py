import re


class MetadataExtractor:
    """
    Extracts statement metadata from raw bank statement text.
    """

    def extract(self, text: str) -> dict:
        metadata = {
            "bank_name": self._extract_bank_name(text),
            "account_holder": self._extract_account_holder(text),
            "account_number": self._extract_account_number(text),
            "ifsc": self._extract_ifsc(text),
            "branch": self._extract_branch(text),
            "statement_period": self._extract_statement_period(text),
        }

        return metadata

    def _extract_bank_name(self, text: str):
        lines = text.splitlines()

        for line in lines:
            line = line.strip()

            if line:
                return line

        return ""

    def _extract_account_holder(self, text: str):
        match = re.search(
            r"Account\s*Name\s*:\s*(.+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""

    def _extract_account_number(self, text: str):
        match = re.search(
            r"Account\s*Number\s*:\s*([0-9]+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""

    def _extract_ifsc(self, text: str):
        match = re.search(
            r"IFSC\s*:\s*([A-Z0-9]+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""

    def _extract_branch(self, text: str):
        match = re.search(
            r"Branch\s*:\s*(.+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""

    def _extract_statement_period(self, text: str):
        match = re.search(
            r"Statement\s*Period\s*:\s*(.+)",
            text,
            re.IGNORECASE,
        )

        if match:
            return match.group(1).strip()

        return ""