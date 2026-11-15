from src.calc import apply_discount


def test_ten_percent_off_200():
    assert apply_discount(200, 10) == 180


def test_no_discount():
    assert apply_discount(100, 0) == 100


def test_half_off():
    assert apply_discount(80, 50) == 40
