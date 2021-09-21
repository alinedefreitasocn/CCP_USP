# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 14:48:48 2019

@author: aline

Como pedido no primeiro vídeo desta semana, escreva uma função
menor_nome(nomes) que recebe uma lista de strings com nome de
pessoas como parâmetro e devolve o nome mais curto presente na lista.

A função deve ignorar espaços antes e depois do nome e deve devolver o menor
nome presente na lista. Este nome deve ser devolvido com a primeira letra
maiúscula e seus demais caracteres minúsculos, independente de como tenha
sido apresentado na lista passada para a função.

Quando houver mais de um nome com o menor comprimento dentre os nomes
na lista, a função deve devolver o primeiro nome com o menor comprimento
presente na lista.
"""

def menor_nome(nomes):
    tamanho = []
    for nome in nomes:
        #tamanho.append(len(nome.decode('utf-8')))
        # no python do curso nao funciona o decode
        if 'é' in nome:
            nome.replace('é', 'e')
        tamanho.append(len(nome.strip()))
    menor = tamanho.index(min(tamanho))
    return nomes[menor].strip().capitalize()


menor_nome([' Aline', 'Gilmara ', 'Karen', 'Luis', 'Lala'])
menor_nome(['jozé', '   Ma         ', 'Karen', 'Luis', 'lala'])
menor_nome(['maria', 'josé', 'PAULO', 'Catarina'])


