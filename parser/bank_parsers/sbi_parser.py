import re

from parser.bank_parsers.base_parser import BaseParser


class SBIParser(BaseParser):
    """
    Parser for SBI OCR statements.
    """

    def parse(self, text: str):
        """
        Parse SBI OCR statement into transaction dictionaries.
        """

        lines = [line.strip() for line in text.splitlines() if line.strip()]

        # -------------------------------------------------
        # Find the start of the transaction table
        # -------------------------------------------------
        start_index = 0

        for i, line in enumerate(lines):
            if (
                "Statement From" in line
                or "Ref No" in line
                or "Value Date" in line
            ):
                start_index = i
                break

        lines = lines[start_index:]

        # -------------------------------------------------
        # Table headers to ignore
        # -------------------------------------------------
        headers = {
            "Ref No",
            "Value Date",
            "Post Date",
            "Details",
            "Debit",
            "Credit",
            "Cheque",
            "Balance",
            "No",
            "ζ Debit",
            "7 Debit",
            "ζ Credit",
            "7 Credit",
        }

        transactions = []

        i = 0

        while i < len(lines):

            line = lines[i]

            # ---------------------------------------------
            # Transaction starts with a date
            # ---------------------------------------------
            if re.fullmatch(r"\d{2}/\d{2}/\d{4}", line):

                transaction = {
                    "date": line,
                    "description": "",
                    "debit": 0.0,
                    "credit": 0.0,
                    "balance": 0.0,
                }

                i += 1

                # Skip second date if present
                if (
                    i < len(lines)
                    and re.fullmatch(r"\d{2}/\d{2}/\d{4}", lines[i])
                ):
                    i += 1

                description = []
                amounts = []

                while i < len(lines):

                    line = lines[i]

                    # Next transaction begins
                    if re.fullmatch(r"\d{2}/\d{2}/\d{4}", line):
                        break

                    # Skip table headers
                    if any(header in line for header in headers):
                        i += 1
                        continue

                    # Skip separator bullets
                    if line in {"•", "-", ":"}:
                        i += 1
                        continue

                    # Remove commas and spaces for number detection
                    cleaned = (
                        line.replace(",", "")
                        .replace(" ", "")
                    )

                    if re.fullmatch(r"\d+\.\d{2}", cleaned):
                        amounts.append(float(cleaned))
                    else:
                        description.append(line)

                    i += 1

                transaction["description"] = " ".join(description)

                # -----------------------------------------
                # Determine debit / credit
                # -----------------------------------------

                desc = transaction["description"].upper()

                if len(amounts) >= 2:

                    balance = amounts[-1]
                    amount = amounts[-2]

                    transaction["balance"] = balance

                    if (
                        "UPV/CR" in desc
                        or "UPI/CR" in desc
                        or "DEP" in desc
                        or "CDM" in desc
                        or "CASH DEPOSIT" in desc
                    ):
                        transaction["credit"] = amount

                    else:
                        transaction["debit"] = amount
                print(
                    f"{transaction['date']} | "
                    f"D:{transaction['debit']} "
                    f"C:{transaction['credit']} "
                    f"B:{transaction['balance']} | "
                    f"{transaction['description'][:60]}"
                )

                transactions.append(transaction)

            else:
                i += 1

        return transactions