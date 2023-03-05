expression = input("Expression: ")
x, y, z = expression.split()

x = int(x)
z = int(z)

match y:
    case "+":
        output = x + z
    case "-":
        output = x - z
    case "*":
        output = x * z
    case "/":
        try:
            output = x / z
        except ZeroDivisionError:
            print("Can not divide an integer to 0!")

print(f"{output:.1f}")