import sys
from pyfiglet import Figlet
import random

def main():

    f = Figlet()
    fonts_list = f.getFonts()

    # Zero command-line arguments
    # Random Font
    if len(sys.argv) == 1:
        text = get_text()
        random_font = random.randint(0, len(fonts_list))
        f.setFont(font = fonts_list[random_font])
        print(f.renderText(text))

    # Two command line arguments
    # Specific Font
    # First argument either -f or --font. Second arrgument is the name of the font.
    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        if sys.argv[2] not in fonts_list:
            sys.exit("Invalid usage")
        else:
            text = get_text()
            font = sys.argv[2]
            f = Figlet(font=font)
            print(f.renderText(text))
    else:
        sys.exit("Invalid usage")

def get_text():
    try:
        t = input("Input: ")
        return t
    except:
        pass

if __name__ == "__main__":
    main()