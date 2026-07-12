class ConfidenceEngine:
    """
    Computes confidence scores for each transaction and
    the overall statement.

    The engine NEVER modifies data.
    It only estimates reliability.
    """

    def evaluate(self, transactions, audit_report):
        results = []

        failed_indexes = {
            issue["index"]
            for issue in audit_report.get("issues", [])
        }

        total_score = 0

        for index, transaction in enumerate(transactions):

            score = 100

            # -----------------------
            # Validation penalties
            # -----------------------
            if not transaction.get("valid", True):
                score -= 20

            # -----------------------
            # Missing Amount
            # -----------------------
            if (
                transaction.get("debit", 0) == 0 and
                transaction.get("credit", 0) == 0
            ):
                score -= 30

            # -----------------------
            # Missing Balance
            # -----------------------
            if transaction.get("balance", 0) == 0:
                score -= 25

            # -----------------------
            # Audit Failure
            # -----------------------
            if index in failed_indexes:
                score -= 20

            score = max(score, 0)

            total_score += score

            results.append({
                "index": index,
                "date": transaction.get("date"),
                "confidence": score
            })

        average = (
            total_score / len(results)
            if results else 0
        )

        return {
            "average_confidence": round(average, 2),
            "transactions": results
        }