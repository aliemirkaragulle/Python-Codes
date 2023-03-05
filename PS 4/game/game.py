import random

def main():
    level = get_num()
    random_int = random.randint(1, level)
    res = game(random_int)
    print(res)

def get_num():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                raise Exception
            else:
                return level
        except:
            pass

def game(num):
    while True:
        try:
            guess = int(input("Guess: "))

            if guess < 1:
                raise Exception

            if guess > num:
                print("Too large!")
            elif guess < num:
                print("Too small!")
            else:
                return "Just right!"
        except:
            pass

if __name__ == "__main__":
    main()