#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 09:22:01 2022

@author: aliemirkaragulle
"""
# GENERATORS

def create_cubes(n):
    for i in range(n):
        yield i**3

for x in create_cubes(10):
    print(x)
    
print(create_cubes(10))
print("\n")



def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
        
for x in gen_fibon(10):
    print(x)
print("\n")



def simple_gen():
    for x in range(3):
        yield x
        
for number in simple_gen():
    print(number)
print("\n")

g = simple_gen()
print(g)

print(next(g))
print(next(g))
print(next(g))
print("\n")



# Converting an iterable object to an iterator
s = "Hello"

# Error!
#print(next(s))

s_iter = iter(s)
print(next(s_iter))
