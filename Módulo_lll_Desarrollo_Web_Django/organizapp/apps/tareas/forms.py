from django import forms
from .models import Homework

class FormHomework(forms.ModelForm):
	class Meta:
		model = Homework
		fields = ('nombreHomework','descripcion','fechaEntrega')