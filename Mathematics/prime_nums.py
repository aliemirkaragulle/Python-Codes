#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 09:39:33 2022

@author: aliemirkaragulle
"""
def count_primes(num):
    prime_nums = [2]
    is_prime = True

    if num < 2:
        return []
    elif num == 2:
        return prime_nums
    else:
        # num = 7
        # i: 3- 4- 5- 6- 7
        for i in range(3, num + 1):
            # j: 2 - 2,3- 2,3,4- 2,3,4,5- 2,3,4,5,6
            for j in range(2, i):
                #print(f"Number: {i} Divided By: {j} Result: {i % j == 0}")
                # Check if the number is prime or not
                if i % j == 0:
                    is_prime = False
            
            # If the number is a prime number, then append it to the list
            if is_prime == True:
                prime_nums.append(i)
            is_prime = True 
    
    return len(prime_nums)