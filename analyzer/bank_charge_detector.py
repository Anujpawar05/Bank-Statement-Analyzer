class BankChargeDetector:
    """
    Detect bank charges from transactions.
    """

    KEYWORDS = [
        "CHARGE",
        "CHARGES",
        "SMS",
        "AMC",
        "ATM",
        "CDM",
        "GST",
    ]

    def detect(self, transactions: list[dict]) -> dict:

        charges = []

        total = 0.0

        for tx in transactions:

            description = tx.get("description", "").upper()

            if any(keyword in description for keyword in self.KEYWORDS):

                charges.append(tx)

                total += tx.get("debit") or 0.0

        return {
            "total_charges": total,
            "charge_count": len(charges),
            "transactions": charges,
        }