import random

def main():
    generate = 0
    score = 0

    level = get_level()
    while generate < 10:
        random_x = generate_integer(level)
        random_y = generate_integer(level)

        question = f"{random_x} + {random_y} = "
        answer = random_x + random_y

        user_answer = int(input(question))

        # Correct
        if answer == user_answer:
            score += 1
            generate += 1

        # False
        else:
            print("EEE")
            try_again = 0
            while try_again < 2:
                user_answer = int(input(question))
                if answer == user_answer:
                    print(f"Number of Trials You Took to Find The Answer: {try_again + 1}")
                    score += 1
                    generate += 1
                    break
                else:
                    print("EEE")
                    try_again += 1

            if try_again == 2:
                    print(f"Correct Answer: {answer}")
                    generate += 1

        print(f"Total Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            return level

        except:
            pass



def generate_integer(level):
    try:
        if level not in [1, 2, 3]:
            raise ValueError

        if level == 1:
            num = random.randint(0, 9)
        elif level == 2:
            num = random.randint(10, 99)
        else:
            num = random.randint(100, 999)
        return num

    except:
        pass

if __name__ == "__main__":
    main()