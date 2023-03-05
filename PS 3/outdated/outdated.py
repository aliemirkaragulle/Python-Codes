def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

    while True:

        try:
            # Numeric Format: MM/DD/YYYY = 9/8/1968
            # Textual Format: September 8, 1968
            # Expected Outcome --> 1968--09--08
            outdated = input("Date: ").strip()

            # Textual Format
            if "," in outdated:
                date = outdated.split(" ")
                day = int(date[1][:-1])
                month = find_month(months, date[0])
                year = date[2]

            # Numeric Format
            elif "/" in outdated:
                date = outdated.split("/")
                day = int(date[1])
                month = int(date[0])
                year = date[2]

            else:
                print("Input format is not correct!")
                raise Exception

            # Logical Errors
            if day > 31:
                print("Maximum allowed number is 31!")
                raise Exception

            if month > 12:
                print("Maximum allowed number is 12!")
                raise Exception

        except:
            print("Error!")

        else:
            # Day
            day = pad_zero(day)

            # Month
            month = pad_zero(month)

            print(year, month, day, sep = "-")
            break



def pad_zero(date):
    if date < 10:
        date = f"0{date}"
    else:
        date = f"{date}"

    return date

def find_month(months, month):
    for i in range(len(months)):
        if months[i] == month:
            month = i + 1
            return month


main()