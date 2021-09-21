# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 13:02:43 2019

@author: aline

Escreva a função conta_letras(frase, contar="vogais"), que recebe como primeiro
parâmetro uma string contendo uma frase e como segundo parâmetro uma outra
string. Este segundo parâmetro deve ser opcional.

Quando o segundo parâmetro for definido como "vogais", a função deve devolver
o numero de vogais presentes na frase. Quando ele for definido como
"consoantes", a função deve devolver o número de consoantes presentes na frase.
Se este parâmetro não for passado para a função, deve-se assumir o valor
"vogais" para o parâmetro.

"""

def vogal(x):
    vogais = ['a', 'e', 'i', 'o', 'u',
              'A', 'E', 'I', 'O', 'U']
    return x in vogais


def conta_letras(frase, contar="vogais"):
    contador = 0
    frase = frase.replace(" ", "")
    if contar == 'vogais':
        for i in frase:
            if vogal(i):
                contador += 1
    elif contar == 'consoantes':
        for i in frase:
            if vogal(i) == False:
                contador += 1
    return contador