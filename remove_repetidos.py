# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 15:07:30 2021

@author: ocnal

Escreva a função remove_repetidos que recebe como parâmetro uma 
lista com números inteiros, verifica se tal lista possui elementos 
repetidos e os remove. A função deve devolver uma lista correspondente 
à primeira lista, sem elementos repetidos. A lista devolvida deve 
estar ordenada.

Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
"""

def remove_repetidos(lista):
    posicao = 0
    print('*' * 5)
    while posicao < len(lista):
        print('Posição {}'.format(posicao))
        print()
        algarismo = lista[posicao]
        print('O algarismo buscado na lista {} é o {}'.format(lista, algarismo))
        if algarismo in lista[posicao + 1:]:
            print('Esse algarismo está repetido. Removendo da lista.')
            del lista[posicao]
            print(lista)
            posicao = posicao
        else:
            posicao = posicao + 1
        print('*' * 5)
        print()
    return sorted(lista)


