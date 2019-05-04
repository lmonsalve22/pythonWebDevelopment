from django.shortcuts import render
from django.http import HttpResponse
from .models import Publication
# Create your views here.

def home(request):
	return render(request,'blog/index.html',{})
	
def verposts(request):
	publicaciones = Publication.objects.all()
	return render(request,'blog/posts.html',{'publicaciones':publicaciones})