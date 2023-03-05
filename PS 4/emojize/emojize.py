import emoji

def main():
    try:
        em = input("Input: ").strip()
        print(emoji.emojize(em))
    except:
        pass

if __name__ == "__main__":
    main()