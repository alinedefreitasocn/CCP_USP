# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 15:46:48 2021

@author: ocnal

Escreva a função soma_elementos que recebe como parâmetro uma 
lista com números inteiros e devolve um número inteiro 
correspondente à soma dos elementos da lista recebida.
"""

def soma_elementos(lista):
    soma = 0
    posicao = 0
    while posicao < len(lista):
        soma = soma + lista[posicao]
        posicao = posicao + 1
    return soma

