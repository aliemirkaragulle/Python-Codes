from sys import argv

if len(argv) == 2:
    print(f"Hello, {argv[1]}")
else:
    print("Hello, World!")
print()

for arg in argv:
    if arg != "argv.py":
        print(arg)
print()

#List Slicing
for arg in argv[1:]:
    print(arg)

for arg in argv[:-1]:
    print(arg)
