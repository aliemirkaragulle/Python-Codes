import pytest
from cs50p import quadratic_expression
from cs50p import discriminant
from cs50p import roots


def main():
    test_quadratic_expression()
    test_discriminant()
    test_roots


def test_quadratic_expression():
    assert quadratic_expression("1x**2") == (1.0, 0.0, 0.0)
    assert quadratic_expression("1x**2+2x") == (1.0, 2.0, 0.0)
    assert quadratic_expression("1x**2-5") == (1.0, 0.0, -5.0)
    assert quadratic_expression("3x**2+2x+1") == (3.0, 2.0, 1.0)
    assert quadratic_expression("-3x**2-2x-1") == (-3.0, -2.0, -1.0)


def test_discriminant():
    a, b, c = quadratic_expression("1x**2")
    assert discriminant(a, b, c) == 0.0

    a, b, c = quadratic_expression("1x**2+2x")
    assert discriminant(a, b, c) == 4.0

    a, b, c = quadratic_expression("1x**2-5")
    assert discriminant(a, b, c) == 20.0

    a, b, c = quadratic_expression("3x**2+2x+1")
    assert discriminant(a, b, c) == -8.0

    a, b, c = quadratic_expression("-3x**2-2x-1")
    assert discriminant(a, b, c) == -8.0


def test_roots():
    a, b, c = quadratic_expression("1x**2")
    assert roots(a, b, c) == 0.0, -0.0

    a, b, c = quadratic_expression("1x**2+2x")
    assert roots(a, b, c) == 0.0, -2.0

    a, b, c = quadratic_expression("1x**2-5")
    assert roots(a, b, c) == 2.23606797749979, -2.23606797749979

    a, b, c = quadratic_expression("3x**2+2x+1")
    assert roots(a, b, c) == "The Equation Has No Real Solutions"

    a, b, c = quadratic_expression("-3x**2-2x-1")
    assert roots(a, b, c) == "The Equation Has No Real Solutions"


if __name__ == "__main__":
    main()