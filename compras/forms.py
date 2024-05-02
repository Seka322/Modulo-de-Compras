from django import forms
from .models import Sucursal, Categoria, ItemCompra
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CompraForm(forms.ModelForm):
	categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(), initial=0)
	sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all(), initial=0)
	class Meta:
		model = ItemCompra
		fields = ['nombre', 'cantidad', 'categoria', 'sucursal']

class RegistroForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']