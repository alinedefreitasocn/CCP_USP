"""
Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e 
devolve uma matriz que represente sua soma caso as matrizes tenham 
dimensões iguais. Caso contrário, a função deve devolver False.
"""
def dimensoes(m):
    linhas = len(m)
    colunas = len(m[0])
    return linhas, colunas

def soma_matrizes(m1, m2):
    if dimensoes(m1) == dimensoes(m2):
        matriz_soma = m1[:]
        for i in range(len(m1)):  # linhas
            for j in range(len(m1[0])):  #colunas
                matriz_soma[i][j] = m1[i][j] + m2[i][j]
        return matriz_soma
    else:
        return False