import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    """
    Converts a 12 Hour Time Format String to 24 Hour Time Format String
    """
    # Conversion Table
    conversion = {f"{i}":f"{i+12}" for i in range(1, 12)}

    # 1 AM - 12 AM
    # If 12 AM -> 00:00
    # Others remain the same!
    am_regex = r"((?:[1][0-2]|[0-9])(?::[0-5][0-9])?) (?:AM)"

    # 1 PM - 12 PM
    # If 12 PM -> 12:00
    # Others + 12
    pm_regex = r"((?:[1][0-2]|[0-9])(?::[0-5][0-9])?) (?:PM)"

    # We need an information on the order of the input
    # Input can be: 8 AM to 7 PM or 7 PM to 8 AM
    # Our output will depend on the ordering of AM and PM
    order_regex = r"(AM|PM)"

    am_match = re.search(am_regex, s, re.IGNORECASE)
    pm_match = re.search(pm_regex, s, re.IGNORECASE)
    order_match = re.search(order_regex, s, re.IGNORECASE)

    # Invalid Sub-Pattern Match
    if am_match is None or pm_match is None or order_match is None:
        raise ValueError

    # The format of am and pm can be either:
    # H AM|PM (8) or HH:MM AM|PM (08:00)
    am = am_match.groups(1)[0]
    pm = pm_match.groups(1)[0]
    order = order_match.groups(1)[0]

    # Invalid Format
    if order == "AM":
        matches = re.search(r"((?:[1][0-2]|[0-9])(?::[0-5][0-9])?) (?:AM) to ((?:[1][0-2]|[0-9])(?::[0-5][0-9])?) (?:PM)", s, re.IGNORECASE)
    else:
        matches = re.search(r"((?:[1][0-2]|[0-9])(?::[0-5][0-9])?) (?:PM) to ((?:[1][0-2]|[0-9])(?::[0-5][0-9])?) (?:AM)", s, re.IGNORECASE)

    if matches is None:
        raise ValueError

    # Invalid Time (8:60 AM...)
    if am == "0" or pm == "0":
        raise ValueError

    # Conversions
    # If our input is in the format H AM|PM, we will add trailing zeroes
    if ":" not in am:
        am = f"{am}:00"
    if ":" not in pm:
        pm = f"{pm}:00"

    # Split hour and minute from am and pm
    am_hour, am_minute = am.split(":")
    pm_hour, pm_minute = pm.split(":")

    # AM Conversions: 12 AM -> 00:00
    if am_hour == "12":
        am_hour = "00"

    # PM Conversions:
    if pm_hour != "12":
        pm_hour = conversion[pm_hour]

    # The format of am_hour and pm_hour should be HH (8 -> 08 and 12 -> 12)
    if len(am_hour) == 1:
        am_hour = f"0{am_hour}"
    if len(pm_hour) == 1:
        pm_hour = f"0{pm_hour}"

    # Output should follow the input order
    # 8 AM to 5 PM -> 08:00 to 17:00
    # 5:30 PM to 7 AM -> 17:30 to 07:00

    if order == "AM":
        return f"{am_hour}:{am_minute} to {pm_hour}:{pm_minute}"
    else:
        return f"{pm_hour}:{pm_minute} to {am_hour}:{am_minute}"


if __name__ == "__main__":
    main()