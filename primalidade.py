# -*- coding: utf-8 -*-
"""
Created on Tue Jun 05 15:03:30 2018

@author: aline
"""

n = int(input("Digite um número inteiro: "))
divisor = n
ndivisores = 0
#nDivisores = []

while divisor > 0:
        divisao = n % divisor
        # se a divisao for exata, n eh divisivel pelo divisor
        if divisao == 0:
            ndivisores = ndivisores + 1
            #nDivisores.append(divisor)
            divisor = divisor - 1
        else:
            divisor = divisor - 1
if ndivisores > 2:
    print("não primo")
else:
    print("primo")

