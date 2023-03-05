from bank import value

def main():
    test_upper()
    test_lower()
    test_mix()
    test_punctuation()
    test_num()


def test_upper():
    assert value("HELLO") == 0
    assert value("HEXAGON") == 20
    assert value("CIAO") == 100

def test_lower():
    assert value("hello") == 0
    assert value("hexagon") == 20
    assert value("ciao") == 100

def test_mix():
    assert value("Hello") == 0
    assert value("Hexagon") == 20
    assert value("Ciao") == 100

def test_punctuation():
    assert value("HELLO.!") == 0
    assert value("HEXAGON.!") == 20
    assert value("CIAO.!") == 100
    assert value(".,!?") == 100

def test_num():
    assert value("500") == 100
    assert value("0") == 100

if __name__ == "__main__":
    main()