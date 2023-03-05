def main():
    expr = input("Expression: ")
    num = convert(expr)
    perc = gauge(num)
    print(perc)



def convert(fraction):
    val = fraction.strip().split("/")
    x, y = val[0], val[1]
    percentage = int((int(x) / int(y)) * 100)
    return percentage



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()