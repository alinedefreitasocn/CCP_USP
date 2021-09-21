# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:56:41 2019

@author: aline

Implemente a função busca(lista, elemento),
 que busca um determinado elemento em uma
 lista e devolve o índice correspondente à
 posição do elemento encontrado. Utilize o
 algoritmo de busca sequencial. Nos casos em
 que o elemento buscado não existir na lista,
 a função deve devolver o booleano False.
"""

def busca(lista, elemento):
    location = -1
    if elemento in lista:
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
    else:
        return False