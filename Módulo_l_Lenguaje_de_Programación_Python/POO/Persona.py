###########
# Clases- Abstracción
###########

class Persona:
	###Atributos
	nombre = "Jorge"
	edad =23
	saludo = "Qué onda"
	#Métodos
	def saludar(self):
		#print(self.saludo," soy una persona")
		#print("%s, soy una persona"%self.saludo) #Placeholder
		return "%s, soy una persona"%self.saludo
jorge = Persona()

print("La edad de %s es: %d"%(jorge.nombre,jorge.edad))
print(jorge.nombre, " dice: ",jorge.saludo)
print(jorge.nombre, " dice: ",jorge.saludar())

jorge.saludar()
