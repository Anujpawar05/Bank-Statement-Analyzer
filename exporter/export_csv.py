import csv
from pathlib import Path


class CSVExporter:
    """
    Exports parsed bank statement transactions to a CSV file.
    """

    def export(self, data, output_path):
        """
        Export transactions to CSV.

        Parameters
        ----------
        data : dict
            Parsed bank statement data.

        output_path : str | Path
            Destination CSV file.

        Returns
        -------
        Path
            Path to the generated CSV file.
        """

        output_path = Path(output_path)

        transactions = data.get("transactions", [])

        with open(output_path, "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(
                [
                    "date",
                    "description",
                    "debit",
                    "credit",
                    "balance",
                ]
            )

            for transaction in transactions:
                writer.writerow(
                    [
                        transaction.get("date", ""),
                        transaction.get("description", ""),
                        transaction.get("debit", 0),
                        transaction.get("credit", 0),
                        transaction.get("balance", 0),
                    ]
                )

        return output_path