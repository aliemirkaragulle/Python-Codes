#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:02:49 2022

@author: aliemirkaragulle
"""
# Inheritance

class Animal:
    def __init__(self, name):
        self.name = name
        print("An animal has been created!")
        
class Dog(Animal):
    """
    def __init__(self, name):
        Animal.__init__(self, name)
    """
    
    def bark(self):
        return self.name + " WOOF!"
    
leon = Dog("Leon")
print(leon.bark())
