from parser.bank_parsers.sbi_parser import SBIParser


def test_sbi_parser_creation():
    """
    SBI parser should be instantiable.
    """
    parser = SBIParser()

    assert parser is not None


def test_sbi_parser_has_parse_method():
    """
    SBI parser should expose a parse method.
    """
    parser = SBIParser()

    assert hasattr(parser, "parse")
    