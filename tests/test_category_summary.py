from analyzer.category_summary import CategorySummary


transactions = [
    {
        "category": "Food",
        "debit": 500.0,
    },
    {
        "category": "Food",
        "debit": 1200.0,
    },
    {
        "category": "Fuel",
        "debit": 3000.0,
    },
    {
        "category": "Shopping",
        "debit": 2500.0,
    },
]


def test_food_total():

    summary = CategorySummary()

    report = summary.generate(transactions)

    assert report["Food"] == 1700.0


def test_fuel_total():

    summary = CategorySummary()

    report = summary.generate(transactions)

    assert report["Fuel"] == 3000.0


def test_shopping_total():

    summary = CategorySummary()

    report = summary.generate(transactions)

    assert report["Shopping"] == 2500.0