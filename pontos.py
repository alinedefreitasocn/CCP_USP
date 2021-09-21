import math

x1 = int(input('Entre com um valor de X1 '))
y1 = int(input('Entre com um valor de Y1 '))
x2 = int(input('Entre com um valor de X2 '))
y2 = int(input('Entre com um valor de Y2 '))

distancia = math.sqrt(((x2-x1)**2)+((y2-y1)**2))

if distancia >= 10:
	print('longe')
else:
	print('perto')