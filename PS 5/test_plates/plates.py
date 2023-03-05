import string

def main():
    plate = input("Plate: ")
    print(is_valid(plate))

def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha):
        return False

    for i in range(len(s)):
        if s[i] in string.punctuation or s[i] == " ":
            return False

    i = 0
    first_digit = 1
    while i < len(s):
        if s[i].isdigit():
            first_digit = s[i]
            break
        else:
            i += 1

    if int(first_digit) == 0:
        return False

    letter_to_number = 0
    number_to_letter = 0
    for i in range(2, len(s)):
        if s[i-1].isalpha() and s[i].isdigit():
            letter_to_number += 1
        if s[i-1].isdigit() and s[i].isalpha():
            number_to_letter += 1

    if letter_to_number + number_to_letter >= 2:
        return False

    return True

if __name__ == "__main__":
    main()