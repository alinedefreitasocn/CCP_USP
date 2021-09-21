# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 16:05:07 2021

@author: ocnal
"""

import re

texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve 
    uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma 
    lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas 
    dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista ### das frases 
    dentro da sentenca ###'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras 
    dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o 
    numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o 
    numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def tamanho_palavras(lista_palavras):
    '''IMPLEMENTADO POR MIM. 
    Tamanho médio de palavra é a soma dos tamanhos 
    das palavras dividida pelo número total de palavras.
    '''
    n_palavras = len(lista_palavras)
    tamanho = 0
    for palavra in lista_palavras:
        tamanho = tamanho + len(palavra)
    palavra_media = tamanho / n_palavras
    return palavra_media

def tamanho_sentenca(lista_sentencas):
    '''
    Tamanho médio de sentença é a soma dos números de caracteres 
    em todas as sentenças dividida pelo número de sentenças 
    (os caracteres que separam uma sentença da outra não devem 
     ser contabilizados como parte da sentença).
    '''
    tamanho = 0
    n_sentencas = len(lista_sentencas)
    for sentenca in lista_sentencas:
        tamanho = tamanho + len(sentenca)
    sentenca_media = tamanho / n_sentencas
    return sentenca_media

def tamanho_frase(lista_frases):
    '''
    Tamanho médio de frase é a soma do número de caracteres em 
    cada frase dividida pelo número de frases no texto  
    (os caracteres que separam uma frase da outra não devem ser 
     contabilizados como parte da frase).
    '''
    tamanho = 0
    n_frases = len(lista_frases)
    for frase in lista_frases:
        tamanho = tamanho + len(frase)
    frase_media = tamanho / n_frases
    return frase_media

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de 
    texto e deve devolver o grau de similaridade nas assinaturas.
    Similaridade:
    Para cada traço linguístico  i i (tamanho médio da palavra, 
    relação type-token etc.) se quer a diferença entre o valor 
    obtido em cada texto dado (a) e o valor típico do texto 
    de uma pessoa infectada (b). Dessa diferença se toma o módulo.
    Somamos os resultados dos 6 traços linguísticos.
    E por final dividimos por 6.
    Perceba que quanto mais similares  a e  b forem, menor será S.
    
    '''
    S = 0
    for i in range(6):
        S = S + abs(as_a[i] - as_b[i])
    S = S / 6
    return S

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver 
    a assinatura do texto.'''
    lista_sentencas = separa_sentencas(texto)
    for sentenca in lista_sentencas:
        lista_frases = separa_frases(sentenca)
        '''
        Complexidade de sentença é o número total de
        frases divido pelo número de sentenças.'''
        complexidade = len(lista_frases) / len(lista_sentencas)
        
        for frase in lista_frases:
            lista_palavras = separa_palavras(frase)
            '''
            Relação Type-Token é o número de palavras diferentes 
            dividido 
            pelo número total de palavras. '''
            
            TypeToken = (n_palavras_diferentes(lista_palavras) / 
                         len(separa_palavras(lista_palavras)))
    
            '''
            Razão Hapax Legomana é o número de palavras que 
            aparecem 
            uma única vez dividido pelo total de palavras.
            '''
            HapaxLegomana = (len(n_palavras_unicas(lista_palavras))/
                              len(separa_palavras(lista_palavras)))
            
            wala = tamanho_palavras(lista_palavras)
   
    return [wala, TypeToken, HapaxLegomana, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos 
    e uma assinatura ass_cp e deve devolver o numero (1 a n)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    for texto in textos:
        ass = calcula_assinatura(texto)
    
    
    pass

""" INICIANDO O PROGRAMA """
''' PRIMEIRO LE OS VALORES DE REFERENCIA DO ALUNO INFECTADO'''
as_b = le_assinatura()

'''DEPOIS LE OS TEXTOS A SEREM AVALIADOS'''
textos = le_textos()


