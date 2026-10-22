from preprocessor.layout_reconstructor import LayoutReconstructor


def test_returns_list():
    reconstructor = LayoutReconstructor()

    result = reconstructor.reconstruct("Hello")

    assert isinstance(result, list)


def test_single_transaction():
    reconstructor = LayoutReconstructor()

    text = (
        "01/04/2025\n"
        "UPI/DR/12345\n"
        "500.00\n"
        "1500.00"
    )

    result = reconstructor.reconstruct(text)

    assert len(result) == 1

    line = result[0]

    assert "01/04/2025" in line
    assert "500.00" in line
    assert "1500.00" in line


def test_multiple_transactions():
    reconstructor = LayoutReconstructor()

    text = (
        "01/04/2025\n"
        "UPI/DR/11111\n"
        "500.00\n"
        "1500.00\n"
        "\n"
        "02/04/2025\n"
        "UPI/CR/22222\n"
        "700.00\n"
        "2200.00"
    )

    result = reconstructor.reconstruct(text)

    assert len(result) == 2

    assert result[0].startswith("01/04/2025")
    assert result[1].startswith("02/04/2025")


def test_ignores_blank_lines():
    reconstructor = LayoutReconstructor()

    text = (
        "\n\n"
        "01/04/2025\n"
        "\n"
        "UPI/DR/12345\n"
        "\n"
        "500.00\n"
        "\n"
        "1500.00\n"
        "\n"
    )

    result = reconstructor.reconstruct(text)

    assert len(result) == 1