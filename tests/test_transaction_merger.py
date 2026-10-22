from preprocessor.transaction_merger import TransactionMerger


def test_single_transaction():
    merger = TransactionMerger()

    lines = [
        "01/04/2025",
        "UPI/DR/12345",
        "Amazon",
        "500.00",
        "1500.00",
    ]

    result = merger.merge(lines)

    assert result == [
        "01/04/2025 UPI/DR/12345 Amazon 500.00 1500.00"
    ]


def test_multiple_transactions():
    merger = TransactionMerger()

    lines = [
        "01/04/2025",
        "UPI/DR/12345",
        "Amazon",
        "500.00",
        "1500.00",
        "02/04/2025",
        "Salary",
        "25000.00",
        "26500.00",
    ]

    result = merger.merge(lines)

    assert len(result) == 2

    assert result[0].startswith("01/04/2025")
    assert result[1].startswith("02/04/2025")


def test_empty_input():
    merger = TransactionMerger()

    assert merger.merge([]) == []


def test_ignores_blank_lines():
    merger = TransactionMerger()

    lines = [
        "",
        "01/04/2025",
        "",
        "UPI",
        "",
        "500.00",
        "",
        "1500.00",
    ]

    result = merger.merge(lines)

    assert len(result) == 1