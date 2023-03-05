import pytest
from fuel import convert
from fuel import gauge

def main():
    test_convert()
    test_convert_exceptions()
    test_gauge()

def test_convert():
    assert convert("3/4") == 75
    assert convert ("1/4") == 25

def test_convert_exceptions():
    with pytest.raises(ValueError):
        convert("Two/Four")
    with pytest.raises(ValueError):
        convert("5/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(45) == "45%"

if __name__ == "__main__":
    main()