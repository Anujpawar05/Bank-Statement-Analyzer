from exporter.workbook_generator import WorkbookGenerator


def test_generate_workbook():

    generator = WorkbookGenerator()

    result = {
        "transactions": [
            {
                "date": "01/04/2026",
                "description": "Salary",
                "debit": None,
                "credit": 50000,
                "balance": 50000,
                "category": "Salary",
                "merchant": "",
            }
        ],
        "analysis": {
            "financial_summary": {
                "total_income": 50000,
                "total_expense": 0,
                "net_cash_flow": 50000,
            }
        },
    }

    workbook = generator.generate(result)

    assert workbook.active.title == "Transactions"
    assert workbook.active["A2"].value == "01/04/2026"
    assert workbook.active["H2"].value == 50000

    summary = workbook["Summary"]

    assert summary["A9"].value == "Total Credits (+)"
    assert summary["B9"].value == 50000

    assert summary["A10"].value == "Total Debits (-)"
    assert summary["B10"].value == 0

    assert summary["A16"].value == "Net Cash Flow"
    assert summary["B16"].value == 50000

    assert summary["A17"].value == "Total Transactions Analyzed"
    assert summary["B17"].value == 1