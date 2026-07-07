from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Transaction:
    """
    Represents a single transaction in a bank statement.
    """

    transaction_id: str

    bank_name: str
    account_number: str

    value_date: Optional[date]
    posting_date: Optional[date]

    description: str
    reference_number: str

    debit: float = 0.0
    credit: float = 0.0
    balance: float = 0.0

    currency: str = "INR"

    category: str = "Uncategorized"

    confidence_score: float = 100.0

    validation_status: bool = True

    remarks: str = ""