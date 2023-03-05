import re
import sys

def main():
    print(validate(input("IPv4 Address: ").strip()))



def validate(ip):

    # Validates till 249.249.249.249
    if re.search(r"^[0-2][0-4]?[0-9]?\.[0-2][0-4]?[0-9]?\.[0-2][0-4]?[0-9]?\.[0-2][0-4]?[0-9]?$", ip):
        return True
    else:
        # Validates from 250.250.250.250 up to 255.255.255.255
        if re.search(r"^[0-2][0-5]?[0-5]?\.[0-2][0-5]?[0-5]?\.[0-2][0-5]?[0-5]?\.[0-2][0-5]?[0-5]?$", ip):
            return True
        else:
            return False

if __name__ == "__main__":
    main()