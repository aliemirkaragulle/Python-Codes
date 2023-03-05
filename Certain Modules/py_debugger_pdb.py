# Python Debugger
import pdb

# You've probably used a variety of print statements to try to find errors in your code. A better way of doing this is by using Python's built-in debugger module (pdb). 
# The pdb module implements an interactive debugging environment for Python programs. 
# It includes features to let you pause your program, look at the values of variables, and watch program execution step-by-step, 
# so you can understand what your program actually does and find bugs in the logic.

# Here we will create an error on purpose, trying to add a list to an integer.
x = [1, 2, 3]
y = 5
z = 10

res_01 = y + z
print(res_01)

# Set a trace using Python Debugger
pdb.set_trace()

res_02 = x + y
print(res_02)

# Great! Now we could check what the various variables were and check for errors. 
# You can use 'q' to quit the debugger.