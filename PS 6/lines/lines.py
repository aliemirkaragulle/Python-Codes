import sys

def main():
    res = lines_of_code()
    print(res)



def lines_of_code():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")


    file_name = sys.argv[1]
    try:
        count = 0
        with open(f"{file_name}") as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if lines[i] == "\n" or lines[i].strip() == "" or lines[i].lstrip().startswith("#"):
                    pass
                else:
                    count += 1
            return count

    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()