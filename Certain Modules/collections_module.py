# Collections Module

# The collections module is a built-in module that implements specialized container data types 
# providing alternative to Python's general purpose built-in containers.
print("Collections Module \n")

from collections import Counter
from collections import defaultdict
from collections import namedtuple

print("Counter \n")
# Counter

# Counter is a dict subclass which helps count hashable objects. 
# Inside of it elements are stored as dictionary keys and the counts of the objects are stored as the value.

# Counter with lists
lst_0 = [1, "a", 2, "b"]
print(Counter(lst_0))

lst_1 = ["ab", "aabb"]
print(Counter(lst_1))

# Counter with strings
str_0 = "aaaabbbbccccdddd"
print(Counter(str_0))

# Counter with texts
s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()

c = Counter(words)
print(c)

# Methods with Counter()
print(c.most_common())

# Common patterns when using the Counter() object
# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts
# d = defaultdict(object)


print("defaultdict \n")
# defaultdict

# defaultdict is a dictionary-like object which provides all methods provided by a dictionary  but takes a first argument (default_factory) as a default data type for the dictionary. 
# Using defaultdict is faster than doing the same using dict.set_default method.
#A defaultdict will never raise a KeyError. Any key that does not exist gets the value returned by the default factory.

# Key Error 
# d_0 = {}
# d_0["One"]

d_1 = defaultdict(object)
d_1["one"]
print(d_1)

d_2 = defaultdict(int)
d_2["one"]
print(d_2)

# Can also initialize with default values:
d = defaultdict(lambda: 0)
d["one"]
print(d)



print("namedtuple \n")
# namedtuple

# The standard tuple uses numerical indexes to access its members. For simple use cases, this is usually enough. 
# On the other hand, remembering which index should be used for each value can lead to errors, especially if the tuple has a lot of fields and is constructed far from where it is used. 

# A namedtuple assigns names, as well as the numerical index, to each member.
# Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. 
# The arguments are the name of the new class and a string containing the names of the elements.
# You can basically think of namedtuples as a very quick way of creating a new object/class type with some attribute fields. For example:
Dog = namedtuple('Dog', ['age', 'breed', 'name'])

# We construct the namedtuple by first passing the object type name (Dog) and then passing a string with the variety of fields as a string with spaces between the field names. 
# We can then call on the various attributes:
sam = Dog(age = 2, breed = 'Lab', name = 'Sammy')
print(sam)
print(sam.age)
print(sam.breed)
print(sam.name)

frank = Dog(age = 2, breed = 'Shepard', name = "Frankie")
print(frank)
print(frank[0])
print(frank[1])
print(frank[2])