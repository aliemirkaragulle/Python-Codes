import re
import sys


def main():
    print(count(input("Text: ").strip()))


def count(s):
    num = 0

    regex = r" ?\bum\b[.,:;?!]?"
    matches = re.findall(regex, s, re.IGNORECASE)

    for match in matches:
        print(match)
        num += 1
    return num


if __name__ == "__main__":
    main()