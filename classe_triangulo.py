# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:43:24 2019

@author: aline

Defina a classe Triangulo cujo construtor recebe 3
valores inteiros correspondentes aos lados a, b e c de
um triângulo.

A classe triângulo também deve possuir um método perimetro,
que não recebe parâmetros e devolve um valor inteiro
correspondente ao perímetro do triângulo.
"""
class Triangulo:
    def __init__(self, ladoa, ladob, ladoc):
        self.a = int(ladoa)
        self.b = int(ladob)
        self.c = int(ladoc)
    def perimetro(self):
        return self.a + self.b + self.c

