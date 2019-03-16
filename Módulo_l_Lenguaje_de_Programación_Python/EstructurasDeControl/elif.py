#####
#ELIF
#####

numero = int(input("Ingresa un número menor a 10: "))

if numero < 10:
	if numero == 4 or numero == 9:
		print(numero, "Tiene raíz exacta")
	elif numero % 2 == 0:
		print(numero," es par")
	elif numero==1 or numero ==3 or numero==5 or numero == 7:
		print(numero," es impar")
	else:
		print("El número es negativo")
else:
	print("¡Dijimos que menor a 10!")

