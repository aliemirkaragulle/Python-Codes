def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Remove the dollar sign and return d as a float
    d = d.strip("$")
    #print(float(d))
    return float(d)

def percent_to_float(p):
    # Remove the percentage sign and return p as a percentage
    p = p.strip("%")
    #print(int(p)/100)
    return int(p)/100

main()