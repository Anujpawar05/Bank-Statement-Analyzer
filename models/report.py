from dataclasses import dataclass

from models.statement import Statement


@dataclass
class Report:
    """
    Final report generated after analysis.
    """

    statement: Statement

    total_bank_charges: float = 0.0

    total_interest: float = 0.0

    validation_passed: bool = True

    total_transactions: int = 0