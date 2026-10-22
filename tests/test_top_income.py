from analyzer.top_income import TopIncome


transactions = [
    {
        "description": "Salary",
        "credit": 50000.0,
    },
    {
        "description": "Interest",
        "credit": 250.0,
    },
    {
        "description": "Cash Deposit",
        "credit": 10000.0,
    },
    {
        "description": "Refund",
        "credit": 3500.0,
    },
]


def test_top_two_income():

    analyzer = TopIncome()

    result = analyzer.generate(transactions, top_n=2)

    assert len(result) == 2
    assert result[0]["description"] == "Salary"
    assert result[1]["description"] == "Cash Deposit"


def test_highest_income():

    analyzer = TopIncome()

    result = analyzer.generate(transactions)

    assert result[0]["credit"] == 50000.0