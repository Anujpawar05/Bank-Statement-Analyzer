from parser.parser_factory import ParserFactory
from parser.bank_parsers.sbi_parser import SBIParser


def test_returns_sbi_parser():

    factory = ParserFactory()

    parser = factory.get_parser("STATE BANK OF INDIA")

    assert isinstance(parser, SBIParser)


def test_unknown_bank_returns_none():

    factory = ParserFactory()

    parser = factory.get_parser("UNKNOWN")

    assert parser is None