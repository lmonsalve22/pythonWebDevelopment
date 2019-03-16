#####
# FOR
#####

lista = [1,2,3,4]
#Foreach
for numero in lista:
	print(numero)

iterador = range(1,100)

#print(iterador,type(iterador))

for i in iterador:
	if i % 2 == 0:
		continue	
	print(i)
