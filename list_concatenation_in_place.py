# List Concatenation In-Place & Not In Place Mutations

l = []
x = l
print(f"Id of l: {id(l)}")
print(f"Id of x: {id(x)}")
print("\n")

# foo += bar --> IN-PLACE MUTATION
l += [1]
print(l)
print(x)
print(f"Id of l: {id(l)}")
print(f"Id of x: {id(x)}")
print("\n")

# foo = foo + bar --> NOT IN-PLACE MUTATION
# l becomes a different object
l = l + [2]
print(l)
print(x)
print(f"Id of l: {id(l)}")
print(f"Id of x: {id(x)}")
print("\n")