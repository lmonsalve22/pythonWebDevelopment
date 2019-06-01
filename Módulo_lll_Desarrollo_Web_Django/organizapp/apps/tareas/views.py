from django.shortcuts import render,get_object_or_404,redirect
from .forms import FormHomework
from .models import Homework
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.

def inicio(request):
	return render(request,'tareas/index_tareas.html')

def agregar_tarea(request):
	if request.method == 'POST':
		form = FormHomework(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.save()
	else:
		form = FormHomework()

	return render(request,'tareas/agregar_tarea.html',{'form':form})

def listar_tarea(request):
	tareas = Homework.objects.all(); 
	return render(request,'tareas/listar_tarea.html',{'tareas':tareas})

def mi_login(request):

	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username,password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				return redirect('inicio')
		else:
			messages.error(request,'Nombre de usuario o contraseña incorrectos')
			return redirect('login')
	else:
		form = AuthenticationForm()
	return render(request,'registration/login.html',{'form':form})


def registrate(request):
	pass