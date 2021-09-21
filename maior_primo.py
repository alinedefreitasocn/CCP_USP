# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 09:10:22 2019

@author: aline
"""

def ehPrimo(k):
    divisor = k
    divisores = 0
    nDivisores = []
    while divisor > 0:
        divisao = k % divisor
        if divisao == 0:
            divisores = divisores + 1
            nDivisores.append(divisor)
            divisor = divisor - 1
        else:
            divisor = divisor - 1
    nDivisores = len(nDivisores)
    return nDivisores


def maior_primo(p):
    while ehPrimo(p) != 2:
        p = p - 1
        ehPrimo(p)
    return p

