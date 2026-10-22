import csv
import tempfile
from pathlib import Path

from exporter.export_csv import CSVExporter


sample = {
    "transactions": [
        {
            "date": "01/04/2026",
            "description": "ATM Withdrawal",
            "debit": 1000,
            "credit": 0,
            "balance": 15000,
        },
        {
            "date": "02/04/2026",
            "description": "Salary",
            "debit": 0,
            "credit": 50000,
            "balance": 65000,
        },
    ]
}


def test_csv_export():

    exporter = CSVExporter()

    with tempfile.TemporaryDirectory() as temp_dir:

        output_file = Path(temp_dir) / "transactions.csv"

        exporter.export(sample, output_file)

        assert output_file.exists()

        with open(output_file, newline="", encoding="utf-8") as file:

            reader = csv.DictReader(file)

            rows = list(reader)

        assert len(rows) == 2
        assert rows[0]["description"] == "ATM Withdrawal"
        assert rows[1]["description"] == "Salary"