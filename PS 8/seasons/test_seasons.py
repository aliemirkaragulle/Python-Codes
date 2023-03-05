from datetime import date
from seasons import min_passed


def main():
    test_min_passed()


def test_min_passed():
    current_date = str(date.today()).split("-")
    current_year, current_month, current_day = int(current_date[0]), int(current_date[1]), int(current_date[2])

    one = f"{current_year - 1}-{current_month}-{current_day}"
    two = f"{current_year - 2}-{current_month}-{current_day}"
    five = f"{current_year - 5}-{current_month}-{current_day}"

    # One Year
    assert min_passed(format_handler(one)) == "Five hundred twenty-five thousand, six hundred minutes"
    # Two Years
    assert min_passed(format_handler(two)) == "One million, fifty-one thousand, two hundred minutes"
    # Five Years
    assert min_passed(format_handler(five)) == "Two million, six hundred twenty-nine thousand, four hundred forty minutes"


def format_handler(d):
    if "-" not in d:
        sys.exit("Invalid Format! (YYYY-MM-DD)")

    date = d.split("-")
    year, month, day = date
    if len(month) != 2:
        f_month = "0" + month
        date[1] = f_month
    if len(day) != 2:
        f_day = "0" + day
        date[2] = f_day
    return "-".join(date)


if __name__ == "__main__":
    main()