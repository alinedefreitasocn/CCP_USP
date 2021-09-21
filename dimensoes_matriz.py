"""
Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj.
"""

def dimensoes(m):
    linhas = len(m)
    colunas = len(m[0])
    print(str(linhas) + 'X' + str(colunas))