from datetime import date
from datetime import datetime
import re
import sys
import inflect


def main():
    # Get the Birth Date in the Format YYYY-MM-DD
    try:
        birth_date = input("Date of Birth: ").strip()
    except:
        pass

    res = min_passed(birth_date)
    print(res)


def min_passed(birth_date):
    # Get the Current Date (YYYY-MM-DD) & Split
    current_date = str(date.today()).split("-")
    # Unpack the List and Cast them to Integers
    current_year, current_month, current_day = int(current_date[0]), int(current_date[1]), int(current_date[2])

    # Instantiation
    current = datetime(current_year, current_month, current_day)
    #print("Current Date:", current)

    # Format Validation
    # Date Format: YYYY-MM-DD
    if matches := re.match(r"^([0-9][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])$", birth_date):
        birth_year, birth_month, birth_day = matches.groups()
    else:
        sys.exit("Invalid Format! YYYY-MM-DD")

    # Instantiation
    birth = datetime(int(birth_year), int(birth_month), int(birth_day))
    #print("Birth Date:", birth)

    # timedelta Object
    # The Time Passed Since Born
    time_passed = current - birth
    #print("Time Passed Since Born:", time_passed)
    #print("Days Passed Since Born:", time_passed.days)

    min_passed = time_passed.days * 24 * 60
    #print("Minutes Passed Since Born:", min_passed)

    p = inflect.engine()
    in_words = p.number_to_words(min_passed, andword="").capitalize()
    return in_words + " minutes"


if __name__ == "__main__":
    main()