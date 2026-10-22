from categorizer.transaction_categorizer import TransactionCategorizer


def test_salary_category():

    categorizer = TransactionCategorizer()

    assert categorizer.categorize("Salary from ABC Pvt Ltd") == "Salary"


def test_food_category():

    categorizer = TransactionCategorizer()

    assert categorizer.categorize("Swiggy Order") == "Food"


def test_fuel_category():

    categorizer = TransactionCategorizer()

    assert categorizer.categorize("Indian Oil Petrol Pump") == "Fuel"


def test_shopping_category():

    categorizer = TransactionCategorizer()

    assert categorizer.categorize("Amazon India") == "Shopping"


def test_unknown_category():

    categorizer = TransactionCategorizer()

    assert categorizer.categorize("Some Random Merchant") == "Other"