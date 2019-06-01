from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Homework(models.Model):
	'''
	Docstring-> Modelo para almacenar tareas
	'''
	autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
	nombreHomework = models.CharField("Nombre de la tarea",max_length=100)
	descripcion = models.TextField("Descripción de la tarea")
	fechaCreacion = models.DateTimeField("Fecha de creación",auto_now_add=True)
	fechaEntrega = models.DateTimeField("Fecha de entrega")
	foto = models.ImageField("Foto de la tarea",upload_to="img/hw/%Y-%m-%d/",blank=True, null=True)
	def __str__(self):
		#return self.nombreHomework 
		return f'{self.autor} {self.nombreHomework}'
