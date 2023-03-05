#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 17:22:23 2021
@author: aliemirkaragulle
"""
""" BINARY SEARCH/ Divide and Conquer Algorithm """

#Generic Algorithm for Item Checking

#Computational Cost: 0(n)
def in_list(x, l):
    for item in l:
        if x == item:
            return True
    
    return False


# l = [2,4,6,8,1,3,5,7,9]
# assert in_list(2, l)
# assert not in_list(10,l)

# for item in range(0,20):
#     result = in_list(item, l)
    
#     print(f"The Item: {item} Presence In The List : {result}")
#     assert result == (item in l)
    
    

#Binary Search

#Prerequisite: Sorted List
#Computational Complexit: O(logn)

#Binary Search Algorithm:
"""
We are searching for the presence of an item "x" in a given list "l".
First, let a variable "m" be the mid-point of the list.
Then;
    1) If l[m] == x, return True
    2) If l[m] > x, left-side of the m should be checked, therefore right-side of m is unnecessary
    3) If l[m] < x, right-side of the m should be checked, therefore left-side of m is unnecessary
Unnecessary sections of the list are removed, therefore m is being updated until termination
Continue until you find the number.
Size of the sub-lists decrease exponentially, (1/2^k).
"""

#Generic Slice Function

def sliced(l, start, end):
    s = []
    for i in range(start, end):
        s += [l[i]] 
    return s

""" First Version of BS """

def binary_search_v1(x, l):
    
    n = len(l)
    
    if n == 0: #The number we are searching for is not contained in the list
        return False
    
    m = n // 2
    
    if x == l[m]: #Conquer/ Stopping Condition
        return True
    
    if l[m] > x: #Search Left
        left_slice = sliced(l, 0, m)
        return binary_search_v1(x, left_slice) #Divide
    
    if l[m] < x: #Search Right
        right_slice = sliced(l, m+1, n)
        return binary_search_v1(x, right_slice) #Divide
        
    
# l = [2, 5, 6, 8, 12, 13, 14]

# for x in range(20):
#     res = binary_search_v1(x, l)
#     print(f"x = {x}, presence = {res}")
#     assert res == (x in l)   



""" Second Version of BS """

#We will create a more efficient version of BS.
#We can optimize the first verion further by not creating so many lists. Let's try to be smarter and avoid copies.
#We have the complete information in the original list, so instead of making copies of lists, 
#we can modify our code to "limit our search for the proper endpoints."

def binary_search_v2(l, x, start = 0, end = None):
    n = len(l)
    
    if end == None: #Setting a mutable object as a default value is not recommended 
        end = n
    
    if start - end == 0: #(start == end): 
        return False
    
    m = (start + end) // 2 
    
    if x == l[m]:   
        return True
    
    if l[m] > x: 
        return binary_search_v2(l, x, start, m)
    
    if l[m] < x:
        return binary_search_v2(l, x, m + 1, end)
 
# l = [2, 5, 6, 8, 12, 13, 14]

# for x in range(20):
#     res = binary_search_v2(x, l)
#     print(f"x = {x}, presence = {res}")
#     assert res == (x in l)



""" Third Version of BS """

#In the third version of BS, our goal is to find the index of the item x in the list l.

def binary_search_v3(l, x, start = 0, end = None):   
    n = len(l)
   
    if end == None: 
        end = n
  
    if start - end == 0:
        return None
    
    m = (start + end) // 2 
    
    if x == l[m]:   
        return m
    
    if l[m] > x: 
        return binary_search_v3(l, x, start, m)
    
    if l[m] < x:
        return binary_search_v3(l, x, m + 1, end)  

l = [2, 5, 6, 8, 12, 13, 14]

for x in range(20):
    ret = binary_search_v3(l, x)
    print(f"x = {x}, index = {ret}")   