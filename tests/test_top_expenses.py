from analyzer.top_expenses import TopExpenses


transactions = [
    {
        "description": "Laptop Purchase",
        "debit": 65000.0,
    },
    {
        "description": "Restaurant",
        "debit": 1200.0,
    },
    {
        "description": "Fuel",
        "debit": 3000.0,
    },
    {
        "description": "Shopping",
        "debit": 8000.0,
    },
]


def test_top_two_expenses():

    analyzer = TopExpenses()

    result = analyzer.generate(transactions, top_n=2)

    assert len(result) == 2
    assert result[0]["description"] == "Laptop Purchase"
    assert result[1]["description"] == "Shopping"


def test_highest_expense():

    analyzer = TopExpenses()

    result = analyzer.generate(transactions)

    assert result[0]["debit"] == 65000.0