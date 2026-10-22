from parser.bank_parsers.base_parser import BaseParser
from parser.bank_parsers.sbi_parser import SBIParser


def test_sbi_is_base_parser():
    parser = SBIParser()

    assert isinstance(parser, BaseParser)