def main():
    try:
        mass = int(input("Enter a mass: "))
    except:
        print("Input should be a number!")
    else:
        c = 300000000
        print(mass * (c ** 2))

main()