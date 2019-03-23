#########
# Calculando áreas
#########
import os 
#Módulo OS, nos va a permitir insteractuar con comandos del sistema


def cuadrado(lado):
	return lado*lado
def triangulo(base,altura):
	return (base*altura)/2
def circulo(radio):
	pi = 3.1416
	return pi*radio**2


#En windows os.system("cls")
while True:
	print("¿Qué área quiéres calcular: ")
	opcion = int(input("Elige la opción: \n1.-Cuadrado\n2.-Triángulo\n3.-Círculo\n4.-Salir"))
	os.system("clear")
	if opcion==1:
		lado = float(input("Ingresa el lado de tu cuadrado: "))
		os.system("clear")
		print(cuadrado(lado))
	elif opcion==2:
		base = float(input("Ingresa la base de tu triángulo: "))
		altura = float(input("Ingresa la altura de tu triángulo: "))
		os.system("clear")
		print(triangulo(base,altura))
	elif opcion==3:
		radio = float(input("Ingresa el radio de tu círculo: "))
		os.system("clear")
		print(circulo(radio)) 
	elif opcion == 4:
		print("Hasta luego!")
		break
	else:
		print("¡Opción incorrecta!\n Intenta de nuevo\n")
