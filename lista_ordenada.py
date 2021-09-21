# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:48:41 2019

@author: aline

Escreva a função ordenada(lista), que recebe uma lista
com números inteiros como parâmetro e devolve o booleano
True se a lista estiver ordenada e False se a lista não
estiver ordenada.
"""

def ordenada(lista):
    for i in range(len(lista)):
        if lista[i] != min(lista[i:]):
            return False
        else:
            return True