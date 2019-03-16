######
# WHILE
######

numero = 0
while numero<20:
	numero = numero+2
	print(numero)
	
numero = 0
while True:
	numero = numero +1
	if numero %2 == 1:
		continue
	print(numero)
	if numero == 20:
		break
