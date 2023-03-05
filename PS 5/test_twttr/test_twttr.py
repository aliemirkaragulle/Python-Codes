from twttr import shorten

def main():
    test_uppercase()
    test_lowercase()
    test_mix()
    test_punctuation()
    test_num()

"""
def test_shorten():
    try:
        assert shorten("Twitter") == "Twttr"
    except AssertionError:
        print("Twitter should have been Twttr")
    try:
        assert shorten("Tweet") == "Twt"
    except AssertionError:
        print("Tweet should have been Twt")
    try:
        assert shorten("TTkk") == "TTkk"
    except AssertionError:
        print("TTKK should have been TTKK")
"""

# PYTEST
def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TWEET") == "TWT"

def test_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("tweet") == "twt"

def test_mix():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Tweet") == "Twt"

def test_punctuation():
    assert shorten("Tweet.") == "Twt."
    assert shorten(".,!?") == ".,!?"

def test_num():
    assert shorten("5") == "5"
    assert shorten("0") == "0"

if __name__ == "__main__":
    main()