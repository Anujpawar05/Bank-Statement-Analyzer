from preprocessor.transaction_line_processor import (
    TransactionLineProcessor
)


def test_line_processor():

    processor = TransactionLineProcessor()

    result = processor.process(
        "01/04/2025 UPV/DR/Zomato 228.06 843.30"
    )

    assert result["dates"] == ["01/04/2025"]

    assert result["amounts"] == [
        "228.06",
        "843.30"
    ]

    assert "Zomato" in result["description"]