from extractor.pdf_loader import PDFLoader
from extractor.document_extractor import DocumentExtractor
from analyzer.confidence_engine import ConfidenceEngine
from parser.bank_detector import BankDetector
from parser.metadata_extractor import MetadataExtractor
from parser.parser_factory import ParserFactory
from parser.ocr_normalizer import OCRNormalizer
from analyzer.analysis_engine import AnalysisEngine
from analyzer.audit_engine import AuditEngine
import time
from categorizer.transaction_categorizer import TransactionCategorizer
from categorizer.nature_classifier import NatureClassifier
from validator.transaction_validator import TransactionValidator
from parser.repair_engine import RepairEngine

class ProcessingPipeline:
    """
    Complete processing pipeline for a bank statement.
    """

    def __init__(self):
        self.document_extractor = DocumentExtractor()
        self.bank_detector = BankDetector()
        self.metadata_extractor = MetadataExtractor()
        self.parser_factory = ParserFactory()
        self.confidence_engine = ConfidenceEngine()
        self.analysis_engine = AnalysisEngine()
        self.audit_engine = AuditEngine()
        self.repair_engine = RepairEngine()
        self.categorizer = TransactionCategorizer()
        self.nature_classifier = NatureClassifier()

    def process(self, pdf_path, password=None):        

        # ---------------------------------
        # Load PDF
        # ---------------------------------
        start = time.time()

        loader = PDFLoader(pdf_path)

        document = loader.load(password=password)
        print(f"PDF Load: {time.time() - start:.2f}s")
        # ---------------------------------
        # Extract Text
        # ---------------------------------
        start = time.time()
        text = self.document_extractor.extract(document)
        print(f"Text Extraction: {time.time()-start:.2f}s")
        # ---------------------------------
        # Normalize OCR
        # ---------------------------------
        start = time.time()

        text = OCRNormalizer.normalize(text)

        print(f"OCR Normalize: {time.time()-start:.2f}s")

        # ---------------------------------
        # Detect Bank
        # ---------------------------------
        start = time.time()

        bank_name = self.bank_detector.detect(text)

        print(f"Bank Detection: {time.time()-start:.2f}s")

        # ---------------------------------
        # Extract Metadata
        # ---------------------------------
        start = time.time()

        metadata = self.metadata_extractor.extract(text)

        print(f"Metadata: {time.time()-start:.2f}s")
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
            start = time.time()

            transactions = parser.parse(text)

            print(f"Parsing: {time.time()-start:.2f}s")

            # ---------------------------------
            # Repair Transactions (reconcile debit/credit)
            # ---------------------------------
            start = time.time()

            repair_report = self.repair_engine.analyze(transactions)

            print(f"Repair: {time.time()-start:.2f}s")

            # ---------------------------------
            # Validate Transactions
            # ---------------------------------
            start = time.time()

            transactions = [
                TransactionValidator.validate(t)
                for t in transactions
            ]

            print(f"Validation: {time.time()-start:.2f}s")

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
            start = time.time()

            audit_report = self.audit_engine.audit(transactions)

            print(f"Audit: {time.time()-start:.2f}s")

        

        # ---------------------------------
        # Confidence Engine
        # ---------------------------------
        start = time.time()

        confidence_report = self.confidence_engine.evaluate(
            transactions,
            audit_report
        )


        print(f"Confidence: {time.time()-start:.2f}s")

        # ---------------------------------
        # Detect Nature of Transactions
        # ---------------------------------
        start = time.time()

        for transaction in transactions:
            desc = transaction.get("description", "")
            transaction["nature"] = self.nature_classifier.classify(desc)

        print(f"Transaction Nature: {time.time()-start:.2f}s")
        # ---------------------------------
        # Financial Analysis
        # ---------------------------------
        start = time.time()

        analysis = self.analysis_engine.analyze(transactions)

        print(f"Analysis: {time.time()-start:.2f}s")

        # Ensure opening and closing balances in metadata
        if transactions:
            if not metadata.get("opening_balance"):
                t0 = transactions[0]
                t0_bal = float(t0.get("balance", 0.0) or 0.0)
                t0_deb = float(t0.get("debit", 0.0) or 0.0)
                t0_crd = float(t0.get("credit", 0.0) or 0.0)
                metadata["opening_balance"] = round(t0_bal + t0_deb - t0_crd, 2)
            if not metadata.get("closing_balance"):
                metadata["closing_balance"] = float(transactions[-1].get("balance", 0.0) or 0.0)

        return {
            "text": text,
            "bank_name": bank_name,
            "metadata": metadata,
            "transactions": transactions,
            "analysis": analysis,
            "audit_report": audit_report,
            "confidence_report": confidence_report,
        }

        