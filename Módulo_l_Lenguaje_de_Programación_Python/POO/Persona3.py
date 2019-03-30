######
# Ejercicio
######

class Persona3:
	def __init__(self,nombre,apellido,edad,estatura,dinero):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.estatura = estatura
		self.dinero = dinero

		#print('Hola soy ',self.nombre," ",self.apellido,", tengo ",self.edad," años y mido ",self.estatura)
		#print("Tengo $",self.dinero," en mi cuenta\n")

	def comer(self,comida):
		print("Hola soy ",self.nombre, " y estoy comiendo: ",comida)
	def informar_saldo(self):
		print("Soy ",self.nombre, " y actualmente tengo $",self.dinero, " pesitos en mi cuenta.")

	def prestar_dinero(self,monto,deudor):
		self.informar_saldo()
		deudor.informar_saldo()
		self.dinero = self.dinero-monto
		deudor.dinero = deudor.dinero+monto
		self.informar_saldo()
		deudor.informar_saldo()
			
jorge = Persona3("Jorge","Chávez",23,1.72,500.0)
ana = Persona3("Anallely","Martínez",20,1.75,10000.0)

ana.prestar_dinero(1000,jorge)
