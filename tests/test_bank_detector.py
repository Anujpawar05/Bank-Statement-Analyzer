import pytest

from parser.bank_detector import BankDetector


@pytest.fixture
def detector():
    return BankDetector()


def test_detect_sbi(detector):
    text = """
    STATE BANK OF INDIA
    Savings Account Statement
    """

    assert detector.detect(text) == "SBI"


def test_detect_bob(detector):
    text = """
    BANK OF BARODA
    Account Statement
    """

    assert detector.detect(text) == "BOB"


def test_detect_hdfc(detector):
    text = """
    HDFC BANK LTD
    Account Statement
    """

    assert detector.detect(text) == "HDFC"


def test_detect_unknown(detector):
    text = """
    Welcome to My Personal Notes
    This is not a bank statement.
    """

    assert detector.detect(text) == "UNKNOWN"