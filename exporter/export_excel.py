from pathlib import Path

from openpyxl import Workbook


class ExcelExporter:
    """
    Exports parsed bank statement transactions to an Excel (.xlsx) file.
    """

    def export(self, data, output_path):
        """
        Export transactions to an Excel workbook.

        Parameters
        ----------
        data : dict
            Parsed bank statement data.

        output_path : str | Path
            Destination Excel file.

        Returns
        -------
        Path
            Path to the generated Excel file.
        """

        output_path = Path(output_path)

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Transactions"

        # Header row
        sheet.append(
            [
                "Date",
                "Description",
                "Debit",
                "Credit",
                "Balance",
            ]
        )

        # Transactions
        transactions = data.get("transactions", [])

        for transaction in transactions:
            sheet.append(
                [
                    transaction.get("date", ""),
                    transaction.get("description", ""),
                    transaction.get("debit", 0),
                    transaction.get("credit", 0),
                    transaction.get("balance", 0),
                ]
            )

        # Auto-adjust column widths
        for column_cells in sheet.columns:
            length = max(len(str(cell.value or "")) for cell in column_cells)
            column_letter = column_cells[0].column_letter
            sheet.column_dimensions[column_letter].width = length + 2

        workbook.save(output_path)

        return output_path