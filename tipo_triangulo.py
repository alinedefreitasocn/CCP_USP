# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:55:58 2019

@author: aline

Defina a classe Triangulo cujo construtor recebe 3
valores inteiros correspondentes aos lados a, b e c de
um triângulo.

A classe triângulo também deve possuir um método perimetro,
que não recebe parâmetros e devolve um valor inteiro
correspondente ao perímetro do triângulo.

Na classe triângulo, definida na Questão 1, escreva o
metodo tipo_lado() que devolve uma string dizendo se o
triângulo é:

isósceles (dois lados iguais)

equilátero (todos os lados iguais)

escaleno (todos os lados diferentes)

Note que se o triângulo for equilátero, a função não
deve devolver isóceles.
"""

class Triangulo:
    def __init__(self, ladoa, ladob, ladoc):
        self.a = int(ladoa)
        self.b = int(ladob)
        self.c = int(ladoc)

    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if ((self.a == self.b != self.c) or
            (self.a == self.c != self.b) or
            (self.c == self.b != self.a)):
            return 'isósceles'
        elif self.a == self.b ==self.c:
            return 'equilátero'
        else:
            return 'escaleno'