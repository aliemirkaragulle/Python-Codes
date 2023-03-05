greeting = input("Greeting: ").lower()
greeting_list = greeting.split()

if "hello" in greeting_list[0]:
    print("$0")
elif greeting_list[0][0] == "h":
    print("$20")
else:
    print("$100")