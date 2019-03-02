# -*-coding:utf-8 -*-
#Indicamos la codificación para el uso de caracteres especiales

#################
#	Cadenas     #
#################

cadena = "Hola"
cadena2 = 'Mundo'
cadenaConComillas = '"Texto entre comillas"'
cadenaLarga = """ Esta es una
cadena larga
o cadenota a secas
"""
cadenaVacia = ""
cadenaCruda = r"Hola \n\t\r"
cadenaNoCruda = "Hola \n\t\r mundo"
print(cadenaNoCruda)
print(cadenaCruda)
print("Tipo de dato: ",type(cadenaCruda))
print("Indexación: ",cadenaCruda[8])
print("Indexación negativa: ",cadenaCruda[-1])
print("Tamaño de la cadena: ",len(cadenaCruda))
print("Concatenación: ",cadenaCruda+cadenaNoCruda)
#Mutabilidad e Inmutabilidad
#cadenaCruda[0] = "J" 
#Las cadenas son inmutables, no soportan asignación por item
print("Repetición: ",cadena*10)
#Slicing
cadena = "H*"+cadena[1:4]
print(cadena)

cadenaUnicode = u"ñ|áéíóúü" #En python 3 no hay problema
print(cadenaUnicode)

#Operaciones con cadenas
cadenaPrueba = "soy de prueba"
print("Búsqueda: ","Hola" in cadenaCruda)
print("Formateo de cadenas: %s,%d"%(cadena,4))
print("Capitalización: ",cadenaPrueba.capitalize())
print("Mayúsculas: ",cadenaPrueba.upper())
print("Minúsculas: ",cadenaPrueba.lower())
print("Split de cadenas: ","hola hola hola".split())