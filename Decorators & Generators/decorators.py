#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:39:01 2022

@author: aliemirkaragulle
"""

# RETURN FUNCTIONS

def hello():
    print("Hello!")
    
hello()
    
greet = hello
greet()

del hello
greet()

print("\n")



def hello_0(name = "Jose"):
    print("The hello_0() function has been executed!")
    
    def greet():
        return "\t This is the greet() inside hello!"
    
    def welcome():
        return "\t This is the welcome() inside hello!"
    
    print(greet())
    print(welcome())
    print("This is the end of the hello_0() function!")

hello_0()
print("\n")



def hello_1(name = "Jose"):
    print("The hello_1() function has been executed!")
    
    def greet():
        return "\t This is the greet() inside hello!"
    
    def welcome():
        return "\t This is the welcome() inside hello!"
    
    print("I am going to return a function!")
    
    if name == "Jose":
        return greet()
    else:
        return welcome()

hello_1()
print("\n")

fun_returned = hello_1()
print(fun_returned)    
print("\n")



def cool():
    
    def super_cool():
        return "I am very cool!"
    
    return super_cool

some_func = cool()
print(some_func())
print("\n")



# PASS IN FUNCTIONS AS ARGUMENTS

def hello_f():
    return "Hi Jose!"

def other(some_def_func):
    print("Other code runs here!")
    print(some_def_func())
    
other(hello_f)
print("\n")



#DECORATOR

def new_decorator(original_func):
    
    def wrap_func():
        """
        This function represents the extra functiionality 
        that you want to decorate this original function with.
        """
        
        print("Some extra code, before the original function!")
        
        original_func()
        
        print("Some extra code, after the original function!")
        
    return wrap_func

def func_needs_decorator():
    print("I want to be decorated!")

decorated_func = new_decorator(func_needs_decorator)
decorated_func()
print("\n")



# On Switch
@new_decorator
def func_needs_decorator_0():
    print("I want to be decorated!")

func_needs_decorator_0()
print("\n")

# Off Switch
#@new_decorator
def func_needs_decorator_1():
    print("I want to be decorated!")

func_needs_decorator_1()
print("\n")
