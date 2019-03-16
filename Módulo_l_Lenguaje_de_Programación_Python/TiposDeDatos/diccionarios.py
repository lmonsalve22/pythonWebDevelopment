##############
# Diccionarios
##############
#Analogía con diccionario de palabras
###Palabra -> Llave
###Significado -> Valor

diccionario = {1:"uno",2:"dos",3:"tres"}

print("Tipo de dato", type(diccionario))
print("Accediendo mediante la llave: ",diccionario[1])
#Agregando nuevo dato
diccionario[4]="cuatro"
print(diccionario)

calificaciones ={"Fernando":9,"Antonio":9,"Mario":10,"Marco":9}

print("La calificación de Fernando es: ",calificaciones["Fernando"])
print("La calificación de Antonio es: ",calificaciones.get("Antonio"))
#No guarda el valor en el diccionario
print("La calificación de Ana es: ",calificaciones.get("ana",10))
#Agregando datos al diccionario
calificaciones.update({"Ana":10})
print("La calificación de Ana es: ",calificaciones.get("Ana"))

alumnos = calificaciones.keys()
listaCalificaciones = calificaciones.values()
print("Mis alumnos son: ", alumnos)
print("Sus calificaciones son: ",listaCalificaciones)

if("Ana" in alumnos):
	print("La calificación de Ana es: ",calificaciones["Ana"])
else:
	print("Ese alumno no existe")

for alumno in alumnos:
	print("Nombre: ",alumno," calicicación: ",calificaciones[alumno])
