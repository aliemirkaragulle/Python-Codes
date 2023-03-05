def camel_to_snake():
    name = input("Enter name: ")
    lower_char = []
    upper_char = []

    # Lower Case Words
    k = 0
    while name[k].islower():
        lower_char.append(name[k])
        k += 1

    # Upper Case Words
    for i in range(len(name)):
        if name[i].isupper():
            upper_char.append("_")
            upper_char.append(name[i].lower())
            j = i + 1
            while j != len(name) and name[j].islower():
                upper_char.append(name[j])
                j += 1

    lowers = "".join(lower_char)
    uppers = "".join(upper_char)
    return lowers + uppers

print(camel_to_snake())