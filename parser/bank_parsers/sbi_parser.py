import re

from parser.bank_parsers.base_parser import BaseParser


class SBIParser(BaseParser):
    """
    Production SBI OCR parser.

    Handles

    • OCR statements
    • Multi-page statements
    • Wrapped descriptions
    • OCR errors
    • Missing debit/credit columns
    • Broken amount formatting
    """

    DATE_PATTERN = re.compile(r"\d{2}/\d{2}/\d{4}")

    AMOUNT_PATTERN = re.compile(
        r"\d{1,3}(?:,\d{3})*\.\d{2}"
    )

    HEADER_KEYWORDS = {
        "Ref No",
        "Value Date",
        "Post Date",
        "Details",
        "Debit",
        "Credit",
        "Cheque",
        "Balance",
        "Statement From",
        "Statement To",
        "Page",
        "Branch",
        "Account",
        "Currency",
    }

    CREDIT_KEYWORDS = [
        "UPV/CR",
        "UPI/CR",
        "DEP",
        "DEPOSIT",
        "CDM",
        "CASH DEPOSIT",
        "INTEREST",
        "REFUND",
        "SALARY",
    ]

    DEBIT_KEYWORDS = [
        "UPV/DR",
        "UPI/DR",
        "ATM",
        "POS",
        "WDL",
        "TRANSFER",
        "PAYTM",
        "GOOGLE PAY",
        "PHONEPE",
        "IMPS",
        "NEFT",
        "RTGS",
    ]

    # -------------------------------------------------------
    # Public parser
    # -------------------------------------------------------

    def parse(self, text: str):
        """
        Parse complete SBI OCR statement.

        Returns
        -------
        list[dict]
        """

        lines = self._prepare_lines(text)

        blocks = self._extract_transaction_blocks(lines)

        transactions = []

        for block in blocks:

            tx = self._parse_transaction(block)

            if tx:
                transactions.append(tx)

        return transactions
    # -------------------------------------------------------
    # Helpers
    # -------------------------------------------------------

    def _prepare_lines(self, text):

        lines = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            if line in {"•", "-", ":"}:
                continue

            lines.append(line)

        return lines


    def _is_date(self, line):

        return bool(self.DATE_PATTERN.fullmatch(line))


    def _find_amounts(self, text):

        matches = self.AMOUNT_PATTERN.findall(text)

        values = []

        for m in matches:

            try:
                values.append(float(m.replace(",", "")))
            except Exception:
                pass

        return values


    def _is_header(self, line):

        for header in self.HEADER_KEYWORDS:

            if header in line:
                return True

        return False


    def _looks_like_credit(self, desc):

        desc = desc.upper()

        return any(word in desc for word in self.CREDIT_KEYWORDS)


    def _looks_like_debit(self, desc):

        desc = desc.upper()

        return any(word in desc for word in self.DEBIT_KEYWORDS)
    