###########
# Método constructor
###########
class Persona2():
	#Definimos el constructor 
	def __init__(self):
		print('Se ha creado una nueva persona')

	def saludar(self):
		print("Hola, soy persona")
	def comer(self):
		print("Estoy comiendo, no molestar")
	def estudiar(self):
		print("Estoy aprendiendo POO")

jorge = Persona2()
ana = Persona2()
antonio = Persona2()

jorge.saludar()
ana.comer()
antonio.estudiar()