# -*- coding: utf-8 -*-
"""
Created on Mon May 28 20:46:54 2018

@author: aline
"""

valorMenor = int(input("Digite o valor de n: "))
fatorial = 1

while valorMenor != 0:
    fatorial = fatorial * valorMenor
    valorMenor = valorMenor - 1
print(fatorial)