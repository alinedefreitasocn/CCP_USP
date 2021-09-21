# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:17:02 2019

@author: aline

Defina a classe Triangulo cujo construtor recebe 3
valores inteiros correspondentes aos lados a, b e c de
um triângulo.

A classe triângulo também deve possuir um método perimetro,
que não recebe parâmetros e devolve um valor inteiro
correspondente ao perímetro do triângulo.


Estes exercícios são baseados na classe Triangulo que você deve ter criado na lista de exercícios obrigatórios desta semana.

Exercício 1: Triângulos retângulos
Escreva, na classe Triangulo, o método retangulo() que devolve True se o triângulo for retângulo, e False caso contrário.
"""

class Triangulo:
    def __init__(self, ladoa, ladob, ladoc):
        self.a = int(ladoa)
        self.b = int(ladob)
        self.c = int(ladoc)
    def retangulo(self):
        lados = sort([self.a, self.b, self.c])
        return lados[2]**2 == (lados[0]** 2) + (lados[1]**2)
