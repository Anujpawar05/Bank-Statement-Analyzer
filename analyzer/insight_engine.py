from analyzer.salary_detector import SalaryDetector
from analyzer.interest_detector import InterestDetector
from analyzer.bank_charge_detector import BankChargeDetector
from analyzer.recurring_detector import RecurringDetector
from analyzer.emi_detector import EMIDetector
from analyzer.cash_deposit_detector import CashDepositDetector
from analyzer.cash_withdrawal_detector import CashWithdrawalDetector
from analyzer.transfer_detector import TransferDetector


class InsightEngine:
    """
    Runs all financial detectors and returns a consolidated report.
    """

    def __init__(self):

        self.salary_detector = SalaryDetector()
        self.interest_detector = InterestDetector()
        self.bank_charge_detector = BankChargeDetector()
        self.recurring_detector = RecurringDetector()
        self.emi_detector = EMIDetector()
        self.cash_deposit_detector = CashDepositDetector()
        self.cash_withdrawal_detector = CashWithdrawalDetector()
        self.transfer_detector = TransferDetector()

    def generate(self, transactions: list[dict]) -> dict:

        return {

            "salary": self.salary_detector.detect(transactions),

            "interest": self.interest_detector.detect(transactions),

            "bank_charges": self.bank_charge_detector.detect(transactions),

            "recurring": self.recurring_detector.detect(transactions),

            "emi": self.emi_detector.detect(transactions),

            "cash_deposits": self.cash_deposit_detector.detect(transactions),

            "cash_withdrawals": self.cash_withdrawal_detector.detect(transactions),

            "transfers": self.transfer_detector.detect(transactions),
        }