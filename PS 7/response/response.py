import validators

def main():
    mail_address = input("What's your email address? ").strip()
    if validators.email(mail_address):
        print("Valid")
    else:
         print("Invalid")

if __name__ == "__main__":
    main()