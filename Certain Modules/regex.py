# Overview of Regular Expressions
import re

# Regular Expressions (sometimes called regex for short) allows a user to search for strings using almost any sort of rule they can come up. 
# For example, finding all capital letters in a string, or finding a phone number in a document.

# Regular expressions are notorious for their seemingly strange syntax. This strange syntax is a byproduct of their flexibility. 
# Regular expressions have to be able to filter out any string pattern you can imagine, which is why they have a complex string pattern format.



# Searching for Basic Patterns
pattern = "number"
text = "The person's phone number is 408-555-1234. Do not call the number tonight!"

# Now we've seen that re.search() will take the pattern, scan the text, and then returns a Match object. 
# If no pattern is found, a None is returned
match = re.search(pattern, text)
print(match)

print(match.span())
print(match.start())
print(match.end())
print("\n")

# But what if the pattern occurs more than once?
# Notice it only matches the first instance. If we wanted a list of all matches, we can use .findall() method:
matches = re.findall(pattern, text)
print(matches)
print(len(matches))
print("\n")

# To get actual match objects, use the iterator:
for match in re.finditer(pattern, text):
    print(match.group())
print("\n")



# Patterns and Quantifiers
matched_01 = re.search(r"\d\d\d-\d\d\d-\d\d\d\d", text)
print(matched_01.group())
print("\n")

matched_02 = re.search(r"\d{3}-\d{3}-\d{4}", text)
print(matched_02.group())