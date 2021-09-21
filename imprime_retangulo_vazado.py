# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 07:39:59 2021

@author: ocnal

Refaça o exercício 1 imprimindo os retângulos sem preenchimento,
 de forma que os caracteres que não estiverem na borda do 
 retângulo sejam espaços.
 
digite a largura: 10
digite a altura: 3
##########
#        #
##########

digite a largura: 2
digite a altura: 2
##
##
"""

largura = int(input('digite a largura: '))
altura = int(input('digite a altura: '))

print(largura * '#')
for a in range(altura-2):
    print('#', end='')
    for l in range(largura-2):
        print(' ', end='')
    print('#', end='')
    print()
print(largura * '#')




