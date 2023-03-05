def main():
    text = "Adieu, adieu, to "
    names = get_names()

    if len(names) == 1:
        print(text + names[0])
    elif len(names) == 2:
        print(text + names[0] + " and " + names[1])
    else:
        for i in range(len(names) - 1):
            text += (f"{names[i]}, ")
        text += "and " + names[-1]
        print(text)



def get_names():
    names = []

    while True:
        try:
            name = input("Name: ")
        except EOFError:
            print("\n")
            break
        except:
            break
        else:
            names.append(name)
    return names

if __name__ == "__main__":
    main()