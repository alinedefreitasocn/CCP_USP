# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

Uma vez iniciado o jogo, a estratégia do computador para 
ganhar consiste em deixar sempre um número de peças que 
seja múltiplo de (m+1) ao jogador. Caso isso não seja 
possível, deverá tirar o número máximo de peças possíveis.

Sejam n o número de peças inicial e m o número máximo de 
peças que é possível retirar em uma rodada.
"""

"""
Uma função computador_escolhe_jogada que recebe, 
como parâmetros, os números n e m descritos acima 
e devolve um inteiro correspondente à próxima jogada 
do computador (ou seja, quantas peças o computador deve 
retirar do tabuleiro) de acordo com a 
estratégia vencedora."""
def computador_escolhe_jogada(n, m):
    # pecas_no_tabuleiro = n - m
    if n > m:
        for pecas_pc in range(1, m + 1, 1):
            pecas_no_tabuleiro = n - pecas_pc
            if pecas_no_tabuleiro % (m+1) == 0:
                return pecas_pc
    else:
        pecas_pc = n
        return pecas_pc
                
        
        
    # while pecas_no_tabuleiro % (m+1) =! 0:
    #     pecas_no_tabuleiro = pecas_no_tabuleiro - (m-1)
        
    # return n
"""
Uma função usuario_escolhe_jogada que recebe os 
mesmos parâmetros, solicita que o jogador informe 
sua jogada e verifica se o valor informado é válido. 
Se o valor informado for válido, a função deve 
devolvê-lo; caso contrário, deve solicitar novamente 
ao usuário que informe uma jogada válida."""

def usuario_escolhe_jogada(n, m):
    pecas_usr = int(input('Quantas peças você vai tirar? '))
    print(' ')
    while (pecas_usr > m) or (pecas_usr > n) or (pecas_usr <= 0):
        print('Oops! Jogada inválida! Tente de novo.')
        print(' ')
        pecas_usr = int(input('Quantas peças você vai tirar? '))
        print(' ')
    return pecas_usr
        

"""
Uma função partida que não recebe nenhum parâmetro, 
solicita ao usuário que informe os valores de n e m e 
inicia o jogo, alternando entre jogadas do computador e 
do usuário (ou seja, chamadas às duas funções anteriores). 
A escolha da jogada inicial deve ser feita em função da 
estratégia vencedora, como dito anteriormente. A cada 
jogada, deve ser impresso na tela o estado atual do jogo, 
ou seja, quantas peças foram removidas na última jogada e
 quantas restam na mesa. Quando a última peça é removida, 
 essa função imprime na tela a mensagem "O computador ganhou!" 
 ou "Você ganhou!" conforme o caso.
 
 Observe que, para isso funcionar, seu programa deve 
 sempre "lembrar" qual é o número de peças atualmente 
 no tabuleiro e qual é o máximo de peças a retirar 
 em cada jogada."""
def partida():
    print(' ')
    n = int(input('Quantas peças?  '))
    m = int(input('Limite de peças por jogada?  '))
    print(' ')
    
    
    # Se n é múltiplo de (m+1), o computador deve ser
    # "generoso" e convidar o jogador a iniciar a partida 
    # com a frase "Você começa!"
    # Caso contrário, o computador toma a inciativa de 
    # começar o jogo, declarando "Computador começa!"
    if n % (m+1) == 0:
        
        print(r'Você começa!')
        print(' ')
        pecas_removidas = usuario_escolhe_jogada(n, m)
        print('Você tirou {} peças.'.format(pecas_removidas))
        player = 'usr'
    else:
        print(r'Computador começa!')
        print(' ')
        pecas_removidas = computador_escolhe_jogada(n, m)
        print('O computador tirou {} peças'.format(pecas_removidas))
        player = 'pc'
    
    # atualiza o numero de pecas no tabuleiro apos a primeira
    # jogada
    n -= pecas_removidas
    
    print(r'Agora restam {} peças no tabuleiro.'.format(n))
    print(' ')
    
    while n != 0:
        
        if player == 'usr':
            pecas_removidas = computador_escolhe_jogada(n, m)
            print('O computador tirou {} peças'.format(pecas_removidas))
            player = 'pc'
        else:
            pecas_removidas = usuario_escolhe_jogada(n, m)
            print('Você tirou {} peças.'.format(pecas_removidas))
            player = 'usr'
        
        n -= pecas_removidas 
        print(r'Agora restam {} peças no tabuleiro.'.format(n))
        print(' ')
    """
    Quando a última peça é removida, essa função imprime 
    na tela a mensagem "O computador ganhou!" ou "Você ganhou!" 
    conforme o caso."""
    if player == 'usr':
        print('Você ganhou!')
    else:
        print('Fim do jogo! O computador ganhou!')
        
    return player

'''
Essa nova função deve realizar três partidas seguidas do 
jogo e, ao final, mostrar o placar dessas três partidas e 
indicar o vencedor do campeonato. O placar deve ser impresso 
na forma'''
def campeonato():
    print(' ')
    print('Voce escolheu um campeonato!')
    pc = 0
    usr = 0
    for j in range(3):
        print(' ')
        print('**** Rodada ', str(j+1), ' ****')
        
        vencedor = partida()
        if vencedor == 'usr':
            usr += 1
        elif vencedor == 'pc':
            pc += 1
    print('**** Final do campeonato! ****')
    print(' ')
    print('Placar: Você {} X {} Computador'.format(usr, pc))

'''
Dado que é possível jogar partidas individuais ou 
campeonatos, seu programa deve começar solicitando ao 
usuário que escolha se prefere jogar apenas uma partida 
(opção 1) ou um campeonato (opção 2).

Atenção: o corretor automático vai verificar se você 
está utilizando exatamente as mensagens pedidas, 
como "Você começa!", "O computador ganhou!" etc. 
Deixe para usar a sua criatividade em outros lugares!    
'''

print(' ')
print('Bem-vindo ao jogo do NIM! Escolha:')
print(' ')
print('1 - para jogar uma partida isolada')
escolha = int(input('2 - para jogar um campeonato '))

if escolha == 1:
    partida()
elif escolha == 2:
    campeonato()
    



