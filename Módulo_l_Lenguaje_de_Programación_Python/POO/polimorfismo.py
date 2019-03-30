#############
#Polimorfismo
#############

class Animal:
	def __init__(self,nombre):
		self.nombre = nombre
	def hablar(self):
		raise NotImplementedError("Debes implementar esto!!")

class Perro(Animal):
	def hablar(self):
		return '"Guaaau!"'

class Gato(Animal):
	def hablar(self):
		return "Miaaauu!"

animales = [Perro('Lucho'),Perro('Firulais'),Gato('Garfield')]

for animal in animales:
	print("Nombre: "+animal.nombre+ " dice: "+animal.hablar())

dinosaurio = Animal("Pie pequeño")

dinosaurio.hablar()