##########
#Tuplas
##########

####Lista -> []
####Tupla -> ()

tupla=(1,"hola",True)
tupla2 = (2,"A",[1,2,3])

print("Tipo de dato: ",type(tupla))
print("Indexación: ",tupla[0])
print("Tamaño: ",len(tupla))
print("Concatenación: ",tupla+tupla2)
print("Repetición: ",tupla*4)
print("Búsqueda: ","A" in tupla2) #Devuelve True si existe
print("Iteración: ")

for elemento in tupla:
	print("Elemento: ",elemento)
#No podemos cambiar elementos de la tupla, pero sí
#elementos mutables que esten dentro
tupla2[2][0]="Hola"
print(tupla2)
#Asignación normal
a,b=0,1
print(a,b)
#Empaquetamiento
tupla3 = 1,2,3,4,5,6
print(tupla3,type(tupla3))
#Desempaquetamiento
a,b,c,d,e,f = tupla3 
print(a,b,c,d,e,f)

tupla4 = (1,4),"hola"
print(tupla4)
#En x se guarda la tupla (1,4) y en y "hola"
x,y=tupla4
print(x,type(x))
print(y,type(y))


