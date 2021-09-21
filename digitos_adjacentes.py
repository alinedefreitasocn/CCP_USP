# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 17:06:04 2018

@author: aline
"""

n = int(input("Digite um número inteiro: "))
digitosIguais = False

while n // 10 > 0:
    digitoAnterior = n % 10
    n = n//10
    digitoAdjacente = n %10
    if digitoAnterior == digitoAdjacente:
        digitosIguais = True

if digitosIguais:
    print("sim")
else:
    print("não")