import tempfile
from pathlib import Path

from openpyxl import load_workbook

from exporter.export_excel import ExcelExporter


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


def test_excel_export():

    exporter = ExcelExporter()

    with tempfile.TemporaryDirectory() as temp_dir:

        output_file = Path(temp_dir) / "transactions.xlsx"

        exporter.export(sample, output_file)

        assert output_file.exists()

        workbook = load_workbook(output_file)

        sheet = workbook.active

        assert sheet["A2"].value == "01/04/2026"
        assert sheet["B3"].value == "Salary"