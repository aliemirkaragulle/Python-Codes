from cs50 import get_string

before = get_string("Before: ")
print("After: ", end = "")

for c in before:
    print(c.upper(), end= "")
print()


before = get_string("Before: ")
after = before.upper()
print(f"After: {after}")

before = get_string("Before: ")
print(f"After: {before.upper()}")