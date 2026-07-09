from extractor.document_extractor import DocumentExtractor
from parser.bank_detector import BankDetector
from parser.metadata_extractor import MetadataExtractor
from parser.parser_factory import ParserFactory
from analyzer.analysis_engine import AnalysisEngine
from categorizer.transaction_categorizer import TransactionCategorizer


class ProcessingPipeline:
    """
    Main orchestration pipeline for processing bank statements.
    """

    def __init__(self):
        self.document_extractor = DocumentExtractor()
        self.bank_detector = BankDetector()
        self.metadata_extractor = MetadataExtractor()
        self.parser_factory = ParserFactory()
        self.analysis_engine = AnalysisEngine()
        self.categorizer = TransactionCategorizer()