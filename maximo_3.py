# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:18:58 2019

@author: aline

Reescreva a função 'maximo' do outro exercício, que devolve o maior valor
entre dois inteiros recebidos, para que ela passe a receber 3 valores
inteiros como parâmetros e devolva o maior dentre eles.
"""


def maximo(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > x and z > y:
        return z
    elif x == y and z == y:
        return y
