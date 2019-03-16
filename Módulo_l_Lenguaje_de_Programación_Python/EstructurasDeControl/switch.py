######
# SWITCH CASE
######

opciones = {1:"Caso 1",2:"Caso 2",3:"Salir"}

llaves = list(opciones.keys())
llaves.sort()


while True:
	print("Menú: ")
	for llave in llaves:
		print("\t%s - %s" %(llave,opciones[llave]))   #PLACEHOLDERS
	seleccion = int(input("Selecciona un caso: "))

	if seleccion in llaves:
		print("Elegiste: ",opciones[seleccion])
		if seleccion == 3:
			break
	else:
		print("(Default) Ingresa una opción válida.")