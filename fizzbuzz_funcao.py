# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:07:22 2019

@author: aline
"""

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0 and n % 5 != 0:
        return 'Fizz'
    elif n % 3 != 0 and n % 5 == 0:
        return 'Buzz'
    else:
        return n


