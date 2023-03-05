def main():
    fuel_remaining = get_remaining_fuel()
    print(fuel_remaining)

def get_remaining_fuel():
    while True:
        try:
            prompt = input("Fraction: ").strip().split("/")

            if int(prompt[0]) > int(prompt[1]):
                raise Exception
            else:
                percentage = (round((int(prompt[0]) / int(prompt[1])) * 100))

        except ValueError:
            print("ValueError!")

        except ZeroDivisionError:
            print("ZeroDivisionError!")

        except:
            pass

        else:
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return str(percentage) + "%"

main()