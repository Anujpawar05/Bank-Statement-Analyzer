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
    assert workbook.active["D2"].value == 50000

    summary = workbook["Summary"]

    assert summary["A13"].value == "Total Income"
    assert summary["B13"].value == 50000

    assert summary["A14"].value == "Total Expense"
    assert summary["B14"].value == 0

    assert summary["A15"].value == "Net Cash Flow"
    assert summary["B15"].value == 50000

    assert summary["A17"].value == "Transactions"
    assert summary["B17"].value == 1