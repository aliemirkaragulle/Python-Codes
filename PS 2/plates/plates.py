import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    if correct_len(s):
        #print("Check 1 Passed")
        if two_letters(s):
                #print("Check 2 Passed")
                if correct_order(s):
                    #print("Check 3 Passed")
                    if no_punctuation(s):
                        #print("Check 4 Passed")
                        return True



def two_letters(s):
    if s[0].isalpha() and s[1].isalpha:
        return True
    else:
        return False



def correct_len(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False



def correct_order(s):
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
    else:
        return True



def no_punctuation(s):
    for i in range(len(s)):
        if s[i] in string.punctuation or s[i] == " ":
            return False
    return True

main()