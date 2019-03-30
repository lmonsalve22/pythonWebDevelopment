#################
# Encapsulamiento
#################

class Animal:
	def __init__(self,nombre,especie,tipo):
		self.nombre=nombre  #publico-> todas las clases pueden acceder a él
		self._especie=especie #protegido->solo las clases que hereden de él pueden accederlo
		self.__tipo=tipo #privado->sólo la clase a la que pertenece tiene acceso
	
	def set_especie(self,especie):
		self._especie=especie
	def get_especie(self):
		return self._especie
	def set_tipo(self,tipo):
		self.__tipo=tipo
	def get_tipo(self):
		return self.__tipo

animal = Animal("Lucho","Canino","Mamífero")
print("Nombre: ",animal.nombre)
print("Especie: ",animal._especie)

animal.set_especie('Canidae')
animal.set_tipo('Carnívoro')

print("Especie: ",animal._especie)
#print("Tipo: ",animal.get_tipo())
#print("Tipo ",animal._Animal__tipo)