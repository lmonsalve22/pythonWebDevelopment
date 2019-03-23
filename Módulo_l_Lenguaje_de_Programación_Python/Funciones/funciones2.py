####################
# Parámetros de funciones
####################

#Parámetros por omisión
"""
def saludar(nombre,mensaje="Qué onda!"):
	print(mensaje,nombre)

saludar(nombre=input("¿Cómo te llamas?"),'Buenos días')
"""

#Parámetros arbitrarios
"""
def recorre_parametros_arbitrarios(parametro_fijo,*arbitrarios):
	#Los parámetros arbitrarios se guardan en una tupla
	print(type(arbitrarios))
	print(parametro_fijo)
	for parametro in arbitrarios:
		print(parametro)

recorre_parametros_arbitrarios('Paramétro fijo','P1','P2','Pn')
"""

#Parámetros kwargs-> keyword arguments
def recorre_parametros_arbitrarios(parametro_fijo,*arbitrarios,**kwargs):
	#Los parámetros arbitrarios se guardan en una tupla
	#Los kwargs se guardan en un diccionario
	print(type(arbitrarios))
	print(type(kwargs))
	print(parametro_fijo)
	for parametro in arbitrarios:
		print(parametro)
	for clave in kwargs:
		print("El valor de, ",clave,"es ",kwargs[clave])

#recorre_parametros_arbitrarios('Soy fijo','Arb1','Arb2','Arbn',clave1='valor1',clave2='valor2',claven='valorn')

#Desempaquetamiento

def calcular(precio,descuento):
	return precio-(precio*descuento/100)

#datos=[1500,10]
#print(calcular(*datos))

datos = {"descuento":10,"precio":1500}

print(calcular(**datos))