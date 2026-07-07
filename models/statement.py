from dataclasses import dataclass, field
from datetime import date
from typing import List

from models.transaction import Transaction


@dataclass
class Statement:
    """
    Represents an entire bank statement.
    """

    bank_name: str

    account_number: str

    account_holder: str

    statement_start: date

    statement_end: date

    opening_balance: float

    closing_balance: float

    transactions: List[Transaction] = field(default_factory=list)