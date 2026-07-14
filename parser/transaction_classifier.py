class TransactionClassifier:
    """
    Classifies transactions into spending categories.
    """

    def __init__(self):
        self.rules = {
            "Food": [
                "ZOMATO",
                "SWIGGY",
                "DOMINOS",
                "PIZZA",
            ],
            "Travel": [
                "UBER",
                "OLA",
                "IRCTC",
                "AIRP",
                "CONFIRM",
            ],
            "Cash Withdrawal": [
                "ATM WDL",
                "WDL",
            ],
            "Cash Deposit": [
                "CDM",
                "CASH DEP",
                "CSH DEP",
            ],
            "Salary": [
                "SALARY",
            ],
            "Interest": [
                "INTEREST",
            ],
        }

    def classify(self, description: str) -> str:
        """
        Return the transaction category.
        """

        description = description.upper()

        for category, keywords in self.rules.items():

            for keyword in keywords:

                if keyword in description:
                    return category

        return "Other"