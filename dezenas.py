entrada = int(input('Digite um número inteiro: '))

dezenas = entrada % 100  # me devolve o resto da divisao por 100
digito = dezenas // 10   # me devolve o resultado da divisao por 10 que sera o digito das dezenas 

print('O dígito das dezenas é', digito)