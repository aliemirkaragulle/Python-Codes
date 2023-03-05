import sys
import csv

def main():
    transform()

def transform():
    try:
        if len(sys.argv) < 3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")

        if sys.argv[1][-4:] != ".csv":
            sys.exit("Invalid file format")
        if sys.argv[2][-4:] != ".csv":
            sys.exit("Invalid file format")

        names = []
        csv_file = sys.argv[1]
        with open(csv_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                surname, name = row["name"].split(",")
                names.append({"first": name, "last": surname, "house": row["house"]})
        #print(names)

        transformed_csv_file = sys.argv[2]
        with open(transformed_csv_file, "w") as new_file:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(new_file, fieldnames = fieldnames)
            writer.writeheader()
            for i in range(len(names)):
                writer.writerow({"first": names[i]["first"].strip(), "last": names[i]["last"].strip(), "house": names[i]["house"].strip()})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

if __name__ == "__main__":
    main()