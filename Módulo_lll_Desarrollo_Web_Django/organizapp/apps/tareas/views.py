from django.shortcuts import render
from .forms import FormHomework
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
