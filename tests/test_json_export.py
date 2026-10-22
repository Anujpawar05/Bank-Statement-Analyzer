import json
import tempfile
from pathlib import Path

from exporter.export_json import JSONExporter


sample = {
    "bank_name": "STATE BANK OF INDIA",
    "account_holder": "JOHN DOE",
    "transactions": [
        {
            "date": "01/04/2026",
            "description": "ATM",
            "debit": 1000,
            "credit": 0,
            "balance": 15000,
        }
    ],
}


def test_json_export():

    exporter = JSONExporter()

    with tempfile.TemporaryDirectory() as temp_dir:

        output_file = Path(temp_dir) / "result.json"

        exporter.export(sample, output_file)

        assert output_file.exists()

        with open(output_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        assert data["bank_name"] == "STATE BANK OF INDIA"

        assert len(data["transactions"]) == 1