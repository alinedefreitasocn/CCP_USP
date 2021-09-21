# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 07:52:24 2021

@author: ocnal

Escreva a função n_primos que recebe como argumento um 
número inteiro maior ou igual a 2 como parâmetro e 
devolve a quantidade de números primos que existem entre 
2 e n (incluindo 2 e, se for o caso, n).

>>>n_primos(2)
1
>>>n_primos(4)
2
>>>n_primos(121)
30
"""

def ehPrimo(x):
    fator = 2
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True
    
    
def n_primos(x):
    count = 0
    if x == 2:
        count = 1
    else:
        while x > 0:
            if ehPrimo(x):
                count = count + 1
            x = x - 1
    return count
    # valor = 2
    # count = 0
    # if x == 2:
    #     return 1
    # while x > 0:  
    #     while x % valor != 0 and valor < x:
    #         print('{} nao é divisivel por {}'.format(x, valor))
    #         valor = valor + 1
    #     if x % valor == 0:
    #         print(r'o {} numero é primo'.format(x))
    #         count = count + 1
    #     x = x - 1

            
    

        