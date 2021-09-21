# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 07:37:48 2021

@author: ocnal

Escreva um programa que recebe como entradas 
(utilize a função input) dois números inteiros 
correspondentes à largura e à altura de um retângulo, 
respectivamente. O programa deve imprimir, usando 
repetições encaixadas (laços aninhados), uma cadeia 
de caracteres que represente o retângulo informado 
com caracteres '#' na saída.

digite a largura: 10
digite a altura: 3
##########
##########
##########
"""

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

for a in range(altura):
    for l in range(largura):
        print('#', end='')
    print()

