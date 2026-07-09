import re


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
    
    def parse_line(self, line: str) -> dict:
        """
        Parse one transaction line into structured fields.
        """

        parts = line.split()

        date = parts[0]

        balance = float(parts[-1])

        amount = float(parts[-2])

        description = " ".join(parts[1:-2])

        return {
            "date": date,
            "description": description,
            "amount": amount,
            "balance": balance,
        }
    
    def parse_debit_line(self, line: str) -> dict:
        """
        Parse a debit transaction line.
        """

        parts = line.split()

        return {
            "date": parts[0],
            "description": " ".join(parts[1:-2]),
            "debit": float(parts[-2]),
            "credit": None,
            "balance": float(parts[-1]),
        }


    def parse_credit_line(self, line: str) -> dict:
        """
        Parse a credit transaction line.
        """

        parts = line.split()

        return {
            "date": parts[0],
            "description": " ".join(parts[1:-2]),
            "debit": None,
            "credit": float(parts[-2]),
            "balance": float(parts[-1]),
        }
    def parse(self, line: str, transaction_type: str = "generic") -> dict:
        """
        Smart transaction parser.

        Parameters
        ----------
        line : str
        Transaction line.

        transaction_type : str
        generic, debit or credit

        Returns
        -------
        dict
        Parsed transaction.
        """

        if transaction_type.lower() == "debit":
            return self.parse_debit_line(line)

        if transaction_type.lower() == "credit":
            return self.parse_credit_line(line)

        return self.parse_line(line)   
    