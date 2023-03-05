# Solution 1
def main():
    text = input("Enter a text: ")
    text = rem_vowels(text)
    print(text)

def rem_vowels(text):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    text_list = []
    rem_vowels_list = []

    for i in range(len(text)):
        text_list.append(text[i])

    for j in range(len(text_list)):
        if text_list[j] not in vowels:
            rem_vowels_list.append(text_list[j])

    return "".join(rem_vowels_list)

main()



# Solution 2
"""
def main():
    text = input("Enter a text: ")
    text = "".join(list(filter(not_vowel, text)))
    print(text)

def not_vowel(char):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if char not in vowels:
        return True
    else:
        return False

main()
"""