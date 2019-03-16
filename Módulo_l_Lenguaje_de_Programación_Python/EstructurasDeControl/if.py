###
# IF
###

numero = int(input("Ingresa un número: "))
#print(numero,type(numero))

residuo = numero % 2 ## Calcuar el residuo

if residuo == 0:
	print(numero," es par")
else:
	print(numero," es impar")
