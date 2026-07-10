from extractor.pdf_loader import PDFLoader
from extractor.document_extractor import DocumentExtractor

from parser.bank_detector import BankDetector
from parser.metadata_extractor import MetadataExtractor
from parser.parser_factory import ParserFactory

from analyzer.analysis_engine import AnalysisEngine
from categorizer.transaction_categorizer import TransactionCategorizer


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
        self.categorizer = TransactionCategorizer()

    def process(self, pdf_path):
        """
        Process a bank statement from start to finish.

        Returns
        -------
        dict
        """

        # -------------------------
        # Load PDF
        # -------------------------
        loader = PDFLoader(pdf_path)
        document = loader.load()

        # -------------------------
        # Extract text
        # -------------------------
        text = self.document_extractor.extract(document)

        # -------------------------
        # Detect bank
        # -------------------------
        bank_name = self.bank_detector.detect(text)

        # -------------------------
        # Extract metadata
        # -------------------------
        metadata = self.metadata_extractor.extract(text)

        # -------------------------
        # Get appropriate parser
        # -------------------------
        parser = self.parser_factory.get_parser(bank_name)
        print(f"Parser selected: {parser}")

        transactions = []

        if parser is not None:
            transactions = parser.parse(text)
            print("\nFIRST 10 PARSED TRANSACTIONS")
            print("=" * 60)

            for t in transactions[:10]:
                print(t)
            print(f"Transactions found: {len(transactions)}")

        # -------------------------
        # Categorize transactions
        # -------------------------
        for transaction in transactions:
            transaction["category"] = self.categorizer.categorize(
                transaction.get("description", "")
            )

        # -------------------------
        # Financial analysis
        # -------------------------
        analysis = self.analysis_engine.analyze(transactions)

        return {
            "text": text,
            "bank_name": bank_name,
            "metadata": metadata,
            "transactions": transactions,
            "analysis": analysis,
            }