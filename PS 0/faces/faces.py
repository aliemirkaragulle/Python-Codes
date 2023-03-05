def main():
    text = input("Enter a text: ")
    print(convert(text))



def convert(text):
    if ":)" in text:
        text = text.replace(":)", "🙂")
    if ":(" in text:
        text = text.replace(":(", "🙁")
    return text

main()