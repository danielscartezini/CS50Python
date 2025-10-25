from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()
    test_convert_negatives()

def test_convert_type():
    assert type(convert("3/4")) is int


def test_convert():
    assert convert("2/3") == 67

    with pytest.raises(ValueError):
        assert convert("cat/dog")

    with pytest.raises(ValueError):
        assert convert("3/2")

    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")

def test_gauge():
    assert gauge(99.0) == 'F'
    assert gauge(100) == 'F'
    assert gauge(1) == 'E'
    assert gauge(75) == '75%'

def test_convert_negatives():
    with pytest.raises(ValueError):
        convert("-1/4")
    with pytest.raises(ValueError):
        convert("1/-4")


if __name__ == "__main__":
    main()
