class TransactionCategorizer:
    """
    Categorizes transactions based on description.
    """

    def categorize(self, description: str) -> str:

        description = description.upper()

        if "SALARY" in description:
            return "Salary"

        if "SWIGGY" in description:
            return "Food"

        if "ZOMATO" in description:
            return "Food"

        if "PETROL" in description:
            return "Fuel"

        if "INDIAN OIL" in description:
            return "Fuel"

        if "AMAZON" in description:
            return "Shopping"

        if "FLIPKART" in description:
            return "Shopping"

        return "Other"