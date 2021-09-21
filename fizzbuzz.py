numero = int(input('Entre com um número qualquer: '))

if ((numero % 5) == 0) and ((numero % 3) == 0):
	print('FizzBuzz')
else:
	print(str(numero))
