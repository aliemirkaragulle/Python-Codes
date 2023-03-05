import pytest
from um import count

def main():
    test_count_single()
    test_count_multiple()
    test_count_sentence()

def test_count_single():
    assert count("um") == 1
    assert count(" um ") == 1
    assert count("um?") == 1
    assert count(" um!") == 1

def test_count_multiple():
    assert count("Um, thanks, um...") == 2
    assert count("Um, help, um, me, um. Um!") == 4


def test_count_sentence():
    assert count("Um, thanks for the album.") == 1
    assert count("Um? Mum? Is this that album where, um, umm, the clumsy alums play drums?") == 2

if __name__ == "__main__":
    main()