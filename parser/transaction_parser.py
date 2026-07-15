import re
from parser.transaction_classifier import TransactionClassifier
from parser.merchant_extractor import MerchantExtractor


class TransactionParser:
    """
    Extract transaction rows from raw bank statement text.
    """

    def __init__(self):
        # Matches lines beginning with a date like:
        # 01/04/26
        # 01-04-2026
        self.date_pattern = re.compile(
            r"^\d{2}[/-]\d{2}[/-]\d{2,4}"
        )
        self.classifier = TransactionClassifier()
        self.merchant_extractor = MerchantExtractor()
        

    def extract_transaction_lines(self, text: str) -> list[str]:
        """
        Return only the lines that appear to be transactions.
        """

        transaction_lines = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            if self.date_pattern.match(line):
                transaction_lines.append(line)

        return transaction_lines
    
    def detect_transaction_type(self, line: str) -> str:
        """
        Detect whether a transaction is debit or credit.

        Returns
        -------
        str
        "debit", "credit", or "generic"
        """

        upper = line.upper()

        if any(keyword in upper for keyword in (
        "UPI/DR",
        "UPV/DR",
        "ATM WDL",
        "WDL",
        "DEBIT",
        "DR/"
        )):
            return "debit"

        if any(keyword in upper for keyword in (
        "UPI/CR",
        "UPV/CR",
        "CASH DEP",
        "CDM",
        "CREDIT",
        "CR/"
        )):
            return "credit"

        return "generic"

    def parse_line(self, line: str) -> dict:
        """
        Parse one transaction line into structured fields.
        """

        parts = line.split()

        date = parts[0]

        balance = self._parse_amount(parts[-1])

        amount = self._parse_amount(parts[-2])

        description = " ".join(parts[1:-2])

        category = self.classifier.classify(description)

        merchant = self.merchant_extractor.extract(description)

        return {
            "date": date,
            "description": description,
            "amount": amount,
            "balance": balance,
            "credit": amount,
            "debit": None,
            "category": category,
            "merchant": merchant,
        }

    def parse_debit_line(self, line: str) -> dict:
        """
        Parse a debit transaction line.
        """

        parts = line.split()

        amount = self._parse_amount(parts[-2])

        description = " ".join(parts[1:-2])

        category = self.classifier.classify(description)

        merchant = self.merchant_extractor.extract(description)

        return {
        "date": parts[0],
        "description": description,
        "amount": amount,          # <-- Added
        "debit": amount,
        "credit": None,
        "balance": self._parse_amount(parts[-1]),
        "category": category,
        "merchant": merchant,
        }

    def parse_credit_line(self, line: str) -> dict:
        """
        Parse a credit transaction line.
        """

        parts = line.split()

        amount = self._parse_amount(parts[-2])

        description = " ".join(parts[1:-2])

        category = self.classifier.classify(description)

        merchant = self.merchant_extractor.extract(description)

        return {
        "date": parts[0],
        "description": description,
        "amount": amount,          # <-- Added
        "debit": None,
        "credit": amount,
        "balance": self._parse_amount(parts[-1]),
        "category": category,
        "merchant": merchant,
        }
    
    def detect_transaction_type(self, line: str) -> str:
        """
        Detect whether a transaction is debit or credit.
        """

        upper = line.upper()

        debit_keywords = [
        "/DR/",
        "UPI/DR",
        "ATM WDL",
        "WDL",
        "DEBIT",
        "WITHDRAWAL",
        "POS",
        "PURCHASE",
        "CHARGE",
        ]

        credit_keywords = [
        "/CR/",
        "UPI/CR",
        "CREDIT",
        "DEPOSIT",
        "CASH DEP",
        "CSH DEP",
        "SALARY",
        "INTEREST",
        "REFUND",
        ]

        for keyword in debit_keywords:
            if keyword in upper:
                return "debit"

        for keyword in credit_keywords:
            if keyword in upper:
                return "credit"

        return "generic"

    def parse(self, line: str, transaction_type: str | None = None) -> dict:
        """
        Parse one transaction.

        If transaction_type is omitted,
        detect it automatically.
        """

        if transaction_type is None:
            transaction_type = self.detect_transaction_type(line)

        if transaction_type.lower() == "debit":
            return self.parse_debit_line(line)

        if transaction_type.lower() == "credit":
            return self.parse_credit_line(line)

        return self.parse_line(line)

    def _parse_amount(self, value: str) -> float:
        """
        Convert OCR amount text into float.

        Examples
        --------
        18,400.00 -> 18400.00
        (500.00)  -> -500.00
        """

        value = value.replace(",", "").strip()

        if value.startswith("(") and value.endswith(")"):
            value = "-" + value[1:-1]

        return float(value)