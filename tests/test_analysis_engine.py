from analyzer.analysis_engine import AnalysisEngine


sample_transactions = [
    {
        "date": "01/04/26",
        "description": "ATM",
        "debit": 1000.0,
        "credit": 0.0,
        "balance": 14000.0,
    },
    {
        "date": "02/04/26",
        "description": "Salary",
        "debit": 0.0,
        "credit": 50000.0,
        "balance": 64000.0,
    },
]


def test_total_debit():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["total_debit"] == 1000.0


def test_total_credit():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["total_credit"] == 50000.0

def test_net_cash_flow():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["net_cash_flow"] == 49000.0

def test_transaction_count():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["transaction_count"] == 2


def test_largest_debit():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["largest_debit"] == 1000.0


def test_largest_credit():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["largest_credit"] == 50000.0

def test_average_debit():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["average_debit"] == 1000.0


def test_average_credit():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["average_credit"] == 50000.0


def test_debit_transaction_count():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["debit_count"] == 1


def test_credit_transaction_count():

    engine = AnalysisEngine()

    summary = engine.analyze(sample_transactions)

    assert summary["credit_count"] == 1