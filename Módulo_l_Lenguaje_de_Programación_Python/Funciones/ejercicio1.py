##################
#Datos personales#
##################
def datos():
	listaDatos = []
	nombre = input("Ingresa tu nombre: ")
	numCuenta = int(input("Ingresa tu número de cuenta: "))
	telefono = int(input("Ingresa tu teléfono: "))
	listaDatos.append(nombre)
	listaDatos.append(numCuenta)
	listaDatos.append(telefono)

	return listaDatos
	
datos_recibidos = datos()
#print(datos_recibidos)

def formato(lista):
	print("Datos sin formato: ",lista)
	print("Datos con formato: ")
	for dato in lista:
		print(lista.index(dato)+1,dato)

formato(datos_recibidos)