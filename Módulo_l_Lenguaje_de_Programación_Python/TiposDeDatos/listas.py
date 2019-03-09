######
# Listas
######
lista = ["hola",4,3.14,True]
lista2 = ["a",2,[1,2,3],["a","b","b"]]

print("Tipo de dato: ",type(lista))
print("Indexación: ",lista[2])
print("Indexación negativa: ",lista[-1])
print("Tamaño de la lista: ",len(lista))
print("Concatenación de listas: ",lista+lista2)
print("Repetición: ",lista*4)
#Asignación por ítem, es permitido porque
#las listas son del tipo mutable
lista[0] = "Adios"
print(lista[0])
print("Búsqueda: ",4 in lista)
print("Elemento de una sublista: ",lista2[2][1])

letras = ["A","B","C","D"]
numeros = [0,1,2,3,4,5,6,7,8,9]
#Ciclo for
for elemento in letras:
	print("Elemento:",elemento)

#Slicing
print("Slicing: ",numeros[1:3])
print("Slicing: ",letras[::3])
print("Slicing: ",numeros[::-1])

#Operaciones con listas
#Inserción
letras.append("E") #Inserta al final
print(letras)
letras.insert(0,"Z") #Inserta al inicio
print(letras)
#Eliminación
letras.pop() #Elimina el último elemento
print(letras)
letras.pop(0) #Elimina el elemento primero
print(letras)
del letras[-1]
print(letras)
#Elimina la primera ocurrencia
letras.append("B")
letras.remove("B")
print(letras)
print("Máximo de la lista numeros", max(numeros))
print("Mínimo de la lista numeros", min(numeros))

#Ordenamiento
numeros.sort()
print("Números ordenados: ",numeros)
numeros.reverse()
print("Números de mayor a menor: ",numeros)

a = [1,2,3,4,5]
b=a[:]
a.reverse()
print("Id de a: ",id(a), "Lista",a) #=>[5,4,3,2,1]
print("Id de b: ",id(b), "Lista",b) 

import copy
c = copy.copy(a)
print("Id de a: ",id(a), "Lista",a) #=>[5,4,3,2,1]

print("Id de c: ",id(c), "Lista",c) 

