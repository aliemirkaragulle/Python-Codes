# Timing Your Code

import time
import timeit

# Sometimes it's important to know how long your code is taking to run, or at least know if a particular line of code is slowing down your entire project. 
# Python has a built-in timing module to do this.



# Timing Start and Stop

# We can try using the time module to simply calculate the elapsed time for the code. 
# Keep in mind, due to the time module's precision, the code needs to take at least 0.1 seconds to complete.

def func_one(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return [str(num) for num in range(n)]

def func_two(n):
    '''
    Given a number n, returns a list of string integers
    ['0','1','2',...'n]
    '''
    return list(map(str, range(n)))

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_one(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(f"It took: {end_time} seconds for the func_one() to execute!")

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = func_two(1000000)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(f"It took: {end_time} seconds for the func_two() to execute!")
print("\n")



# Timeit Module

# What if we have two blocks of code that are quite fast, the difference from the time.time() method may not be enough to tell which is fater. 
# In this case, we can use the timeit module.
#The timeit module takes in two strings, a statement (stmt) and a setup. 
# It then runs the setup code and runs the stmt code some n number of times and reports back average length of time it took.

setup = '''
def func_one(n):
    return [str(num) for num in range(n)]
'''
stmt = 'func_one(100)'

time_func_one = timeit.timeit(stmt,setup,number=100000)
print(f"It took: {time_func_one} seconds for the func_one() to execute!")

setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
stmt2 = 'func_two(100)'

time_func_two = timeit.timeit(stmt2,setup2,number=100000)
print(f"It took: {time_func_two} seconds for the func_two() to execute!")