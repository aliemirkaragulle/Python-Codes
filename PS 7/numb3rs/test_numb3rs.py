from numb3rs import validate

def main():
    test_validate_valid()
    test_validate_invalid()



def test_validate_valid():
    assert validate("255.255.255.255") == True
    assert validate("1.1.0.0") == True

def test_validate_invalid():
    assert validate("512.512.512.512") == False
    assert validate("1.2.4.1000") == False
    assert validate("2.555.555.555") == False
    assert validate("cat") == False

if __name__ == "__main__":
    main()