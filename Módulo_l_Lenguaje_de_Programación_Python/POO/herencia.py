##########
# Herencia
##########

class Vehiculo:
	def __init__(self,color,ruedas):
		self.color = color
		self.ruedas = ruedas

	##Método mágico
	def __str__(self):
		return "Color: {}, {} ruedas".format(self.color,self.ruedas)

class Auto(Vehiculo):
	def __init__(self,color,ruedas,velocidad,marca):
		Vehiculo.__init__(self,color,ruedas)
		self.velocidad = velocidad
		self.marca = marca
	
	def __str__(self):
		return Vehiculo.__str__(self) + ", {} km/h, marca {}".format(self.velocidad,self.marca)
		

bochito = Auto("Amarillo",4,80,"Volkswagen")

print(bochito)