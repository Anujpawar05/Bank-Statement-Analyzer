from utils.amount_reconstructor import AmountReconstructor


def test_two_amounts():
    reconstructor = AmountReconstructor()

    result = reconstructor.split("228.06843.30")

    assert result == ["228.06", "843.30"]


def test_large_amount():
    reconstructor = AmountReconstructor()

    result = reconstructor.split("13500.0013813.30")

    assert result == ["13500.00", "13813.30"]


def test_single_amount():
    reconstructor = AmountReconstructor()

    result = reconstructor.split("500.00")

    assert result == ["500.00"]


def test_no_amount():
    reconstructor = AmountReconstructor()

    result = reconstructor.split("HELLO WORLD")

    assert result == []