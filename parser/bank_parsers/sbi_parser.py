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

    def parse(self, text: str):
        """
        Parse complete SBI OCR statement.
        """

        lines = self._prepare_lines(text)

        blocks = self._extract_transaction_blocks(lines)

        transactions = []

        for block in blocks:

            tx = self._parse_transaction(block)

            if not tx:
                continue

            transactions.append(tx)

        return transactions
    
        # ---------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------

    def _prepare_lines(self, text):
        """
        Clean OCR text and return usable lines.
        """

        lines = []

        for line in text.splitlines():

            line = line.strip()

            if not line:
                continue

            if line in {"•", "-", ":"}:
                continue

            lines.append(line)

        return lines

    def _extract_transaction_blocks(self, lines):
        """
        Split OCR text into transaction blocks.

        Each transaction starts with a date.
        Consecutive duplicate dates belong to the same transaction.
        """

        blocks = []

        current = []
        started = False

        for line in lines:

        # Ignore everything before first transaction
            if not started:
                if self._is_date(line):
                    started = True
                else:
                    continue

        # -------------------------
        # New transaction detected
        # -------------------------
            if self._is_date(line):

            # Consecutive duplicate date
                if (
                    current
                    and len(current) == 1
                    and self._is_date(current[0])
                ):
                    continue

            # Save previous transaction
                if current:

                # Ignore blocks containing only a date
                    if len(current) > 1:
                        blocks.append(current)

                current = [line]

            else:

                current.append(line)

        # Save final block
        if current and len(current) > 1:
            blocks.append(current)

        return blocks

    def _is_date(self, line):

        return bool(self.DATE_PATTERN.fullmatch(line))

    def _find_amounts(self, text):
        """
        Extract monetary values from OCR text.

        Handles OCR issues like:
        - 1,250.00
        - 1250.00
        - 5,002. 10
        - 5002. 10
        - 5 002.10
        """

        # Remove commas
        text = text.replace(",", "")

    # Fix OCR space before decimal digits
        text = re.sub(
            r"(\d)\.\s+(\d{2})",
            r"\1.\2",
            text,
        )

    # Fix OCR spaces inside numbers
        text = re.sub(
            r"(\d)\s+(\d+\.\d{2})",
            r"\1\2",
            text,
        )

    # Collapse multiple spaces
        text = re.sub(
            r"\s+",
            " ",
            text,
        )

        matches = re.findall(
            r"\b\d{1,9}\.\d{2}\b",
            text,
        )

        filtered = []

        for value in matches:

            try:

                number = float(value)

        # Ignore OCR-created fake amounts
                if number > 100000:
                    continue

                filtered.append(number)

            except ValueError:
                pass

        return filtered

        return [float(value) for value in matches]
     
    def _is_header(self, line):

        for header in self.HEADER_KEYWORDS:

            if header in line:
                return True

        return False

    def _looks_like_credit(self, description):

        description = description.upper()

        return any(
            keyword in description
            for keyword in self.CREDIT_KEYWORDS
        )

    def _looks_like_debit(self, description):

        description = description.upper()

        return any(
            keyword in description
            for keyword in self.DEBIT_KEYWORDS
        )
    
        # ---------------------------------------------------------
    # Transaction Parsing
    # ---------------------------------------------------------

    def _parse_transaction(self, block):
        """
        Parse one transaction block into a transaction dictionary.
        """

        if not block:
            return None

        tx = {
            "date": block[0],
            "description": "",
            "debit": 0.0,
            "credit": 0.0,
            "balance": 0.0,
        }

        description_parts = []
        numbers = []

        # Skip the first line because it is the transaction date
        for line in block[1:]:

            # Ignore repeated dates
            if self._is_date(line):
                continue

            # Ignore table headers
            if self._is_header(line):
                continue

            amounts = self._find_amounts(line)

            if amounts:

                numbers.extend(amounts)

                cleaned = line

                # Remove detected amounts from description
                for amount in self.AMOUNT_PATTERN.findall(line):
                    cleaned = cleaned.replace(amount, "")

                cleaned = " ".join(cleaned.split())

                if cleaned:
                    description_parts.append(cleaned)

            else:

                description_parts.append(line)

        tx["description"] = " ".join(description_parts).strip()

        self._assign_amounts(tx, numbers)

        # Development debug output
        print(
            f"{tx['date']} | "
            f"D:{tx['debit']} "
            f"C:{tx['credit']} "
            f"B:{tx['balance']} | "
            f"{tx['description'][:80]}"
        )

        return tx

    def _assign_amounts(self, tx, numbers):
        """
        Assign debit, credit and balance using extracted amounts.
        """

        if not numbers:
            return

        description = tx["description"]

        # Typical SBI pattern:
        # debit balance
        # credit balance
        if len(numbers) == 1:

            amount = numbers[0]

        elif len(numbers) >= 2:

            tx["balance"] = numbers[-1]
            amount = numbers[-2]

        else:
            return

            amount = numbers[0]

        desc = description.upper()

        if self._looks_like_credit(desc):

            tx["credit"] = amount

        elif self._looks_like_debit(desc):

            tx["debit"] = amount

        elif "UPV/CR" in desc or "UPI/CR" in desc:

            tx["credit"] = amount

        elif "UPV/DR" in desc or "UPI/DR" in desc:

            tx["debit"] = amount

        elif "DEPOSIT" in desc or "CDM" in desc:

            tx["credit"] = amount

        elif "REFUND" in desc or "INTEREST" in desc:

            tx["credit"] = amount

        else:

            tx["debit"] = amount

            # Debug parser decisions
        if tx["debit"] == 0 and tx["credit"] == 0:
            print(
                f"[UNCLASSIFIED] {tx['date']} | {tx['description']}"
        )

        if tx["balance"] == 0:
            print(
                f"[NO BALANCE] {tx['date']} | {tx['description']}"
        )

        if len(numbers) >= 3:
            print(
                f"[MULTIPLE AMOUNTS] {tx['date']} | {numbers} | {tx['description']}"
            )

        