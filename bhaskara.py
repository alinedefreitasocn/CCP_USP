import math

a = int(input('Entre com um número qualquer: '))
b = int(input('Entre com um número qualquer: '))
c = int(input('Entre com um número qualquer: '))


if (b**2) == (4*a*c):
	delta = math.sqrt((b**2)-(4*a*c))
	X = (-b+delta)/2*a
	print('a raiz desta equação é', X)
elif (b**2) > (4*a*c):
	delta = math.sqrt((b**2)-(4*a*c))
	X = (-b-delta)/2*a
	Y = (-b+delta)/2*a
	print('as raízes da equação são', X, 'e', Y)
else:
	print('esta equação não possui raízes reais')

