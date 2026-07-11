from extractor.pdf_loader import PDFLoader
from extractor.document_extractor import DocumentExtractor

from parser.bank_detector import BankDetector
from parser.metadata_extractor import MetadataExtractor
from parser.parser_factory import ParserFactory

from analyzer.analysis_engine import AnalysisEngine
from analyzer.audit_engine import AuditEngine

from categorizer.transaction_categorizer import TransactionCategorizer
from validator.transaction_validator import TransactionValidator


class ProcessingPipeline:
    """
    Complete processing pipeline for a bank statement.
    """

    def __init__(self):
        self.document_extractor = DocumentExtractor()
        self.bank_detector = BankDetector()
        self.metadata_extractor = MetadataExtractor()
        self.parser_factory = ParserFactory()

        self.analysis_engine = AnalysisEngine()
        self.audit_engine = AuditEngine()

        self.categorizer = TransactionCategorizer()

    def process(self, pdf_path):
        """
        Process a bank statement from start to finish.

        Returns
        -------
        dict
        """

        # ---------------------------------
        # Load PDF
        # ---------------------------------
        loader = PDFLoader(pdf_path)
        document = loader.load()

        # ---------------------------------
        # Extract Text
        # ---------------------------------
        text = self.document_extractor.extract(document)

        # ---------------------------------
        # Detect Bank
        # ---------------------------------
        bank_name = self.bank_detector.detect(text)

        # ---------------------------------
        # Extract Metadata
        # ---------------------------------
        metadata = self.metadata_extractor.extract(text)

        # ---------------------------------
        # Select Parser
        # ---------------------------------
        parser = self.parser_factory.get_parser(bank_name)
        print(f"Parser selected: {parser}")

        transactions = []
        audit_report = {
            "passed": 0,
            "failed": 0,
            "issues": []
        }

        if parser is not None:

            # ---------------------------------
            # Parse Transactions
            # ---------------------------------
            transactions = parser.parse(text)

            # ---------------------------------
            # Validate Transactions
            # ---------------------------------
            transactions = [
                TransactionValidator.validate(t)
                for t in transactions
            ]

            print("\nVALIDATION REPORT")
            print("=" * 60)

            valid = 0
            invalid = 0

            for transaction in transactions:

                if transaction["valid"]:
                    valid += 1
                else:
                    invalid += 1
                    print(
                        f"{transaction['date']} -> "
                        f"{transaction['warnings']}"
                    )

            print()
            print(f"Valid Transactions   : {valid}")
            print(f"Invalid Transactions : {invalid}")
            print(f"Total Transactions   : {len(transactions)}")

            # ---------------------------------
            # Audit Transactions
            # ---------------------------------
            audit_report = self.audit_engine.audit(transactions)

            print("\nAUDIT REPORT")
            print("=" * 60)

            print(f"Passed Checks : {audit_report['passed']}")
            print(f"Failed Checks : {audit_report['failed']}")

            if audit_report["issues"]:

                print("\nDetected Issues\n")

                for issue in audit_report["issues"]:
                    print(
                        f"[{issue['index']}] "
                        f"{issue['date']} | "
                        f"Expected={issue['expected_balance']:.2f} | "
                        f"Actual={issue['actual_balance']:.2f} | "
                        f"Difference={issue['difference']:.2f}"
                    )

            else:
                print("No balance inconsistencies detected.")

        # ---------------------------------
        # Categorize Transactions
        # ---------------------------------
        for transaction in transactions:
            transaction["category"] = self.categorizer.categorize(
                transaction.get("description", "")
            )

        # ---------------------------------
        # Financial Analysis
        # ---------------------------------
        analysis = self.analysis_engine.analyze(transactions)

        return {
            "text": text,
            "bank_name": bank_name,
            "metadata": metadata,
            "transactions": transactions,
            "analysis": analysis,
            "audit_report": audit_report,
        }