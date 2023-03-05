answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

match answer.lower().strip():
    case "42" | "forty two" | "forty-two":
        print("Yes")
    case other_answers:
        print("No")

"""
answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")

if answer.lower().strip() == "42" or answer.lower().strip() == "forty-two" or answer.lower().strip() == "forty two":
    print("Yes")
else:
    print(("No"))
"""