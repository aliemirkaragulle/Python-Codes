# Binomial Distribution
import random
import matplotlib.pyplot as plt

def main():
    num = get_num()
    res = toss(num)
    print(res)



def get_num():
    while True:
        try:
            n = int(input("Number of Times: "))
            return n
        except:
            print("Invalid Input")



def toss(num):
    i = 0
    res = {"Heads": 0, "Tails": 0}
    while i < num:
        coin = random.choice(["Heads", "Tails"])
        res[coin] += 1
        i += 1
    return res

main()
