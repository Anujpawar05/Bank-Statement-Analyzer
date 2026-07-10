from datetime import datetime
import re


class TransactionValidator:

    @staticmethod
    def is_valid_date(date_str):
        try:
            datetime.strptime(date_str, "%d/%m/%Y")
            return True
        except Exception:
            return False

    @staticmethod
    def is_number(value):
        return isinstance(value, (int, float))

    @staticmethod
    def contains_garbage(text):
        garbage = [
            "ζ",
            "•",
            "III",
            "!",
            ":",
            "+MOD",
            "0+"
        ]

        for g in garbage:
            if g in text:
                return True

        return False

    @staticmethod
    def validate(transaction):

        warnings = []

        # ------------------------
        # Date Validation
        # ------------------------
        if not TransactionValidator.is_valid_date(
                transaction.get("date", "")
        ):
            warnings.append("Invalid date")

        # ------------------------
        # Amount Validation
        # ------------------------
        debit = transaction.get("debit", 0)
        credit = transaction.get("credit", 0)

        if not TransactionValidator.is_number(debit):
            warnings.append("Debit is not numeric")

        if not TransactionValidator.is_number(credit):
            warnings.append("Credit is not numeric")

        if debit < 0:
            warnings.append("Negative debit")

        if credit < 0:
            warnings.append("Negative credit")

        if debit > 0 and credit > 0:
            warnings.append("Both debit and credit present")

        if debit == 0 and credit == 0:
            warnings.append("Missing transaction amount")

        # ------------------------
        # Balance Validation
        # ------------------------
        balance = transaction.get("balance")

        if not TransactionValidator.is_number(balance):
            warnings.append("Invalid balance")

        # ------------------------
        # Description Validation
        # ------------------------
        desc = transaction.get("description", "")

        if len(desc.strip()) < 5:
            warnings.append("Description too short")

        if TransactionValidator.contains_garbage(desc):
            warnings.append("OCR garbage detected")

        transaction["valid"] = len(warnings) == 0
        transaction["warnings"] = warnings

        return transaction