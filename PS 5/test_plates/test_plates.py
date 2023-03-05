from plates import is_valid

def main():
    test_is_valid()
    test_correct_length()
    test_two_letters()
    test_correct_order()
    test_no_punctuation()

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_correct_length():
    assert is_valid("CS500") == True
    assert is_valid("1111111111") == False

def test_two_letters():
    assert is_valid("CS50") == True
    assert is_valid("CS500000") == False
    assert is_valid("500000") == False
    assert is_valid("50CS") == False

def test_correct_order():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_no_punctuation():
    assert is_valid("CS50.") == False
    assert is_valid(".,!?") == False

if __name__ == "__main__":
    main()