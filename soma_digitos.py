# -*- coding: utf-8 -*-
"""
Created on Mon May 28 21:13:17 2018

@author: aline
soma_digitos
"""

entrada = int(input("Digite um número inteiro: "))
soma = 0

while entrada != 0:
    algarismo = entrada % 10
    soma = soma + algarismo
    entrada = entrada // 10
print(soma)