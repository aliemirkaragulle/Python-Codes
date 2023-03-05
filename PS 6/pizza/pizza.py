import sys
import csv
from tabulate import tabulate

def main():
    table = table_from_csv()
    print(table)

def table_from_csv():
    try:
        if len(sys.argv) != 2:
            sys.exit("Invalid Length!")

        if sys.argv[1][-4:] != ".csv":
            sys.exit("Invalid File Format!")

        file_name = sys.argv[1]
        table = []

        with open(f"{file_name}") as file:
            reader = csv.reader(file)
            for rows in reader:
                table.append(rows)

            return tabulate(table[1:], headers = table[0], tablefmt = "grid")

    except FileNotFoundError:
        sys.exit("File Does Not Exist!")

if __name__ == "__main__":
    main()