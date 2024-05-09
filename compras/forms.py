from django import forms
from .models import Sucursal, Categoria, ItemCompra
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CompraForm(forms.ModelForm):
	sucursal = forms.ModelChoiceField(queryset=Sucursal.objects.all(), required=True)
    producto = forms.ModelChoiceField(queryset=ItemProveedor.objects.filter(unidades__gt=0), required=True)
	
	def __init__(self, *args, **kwargs):
		productos = kwargs.pop('productos', None)
		super(CompraForm, self).__init__(*args, **kwargs)
		if productos is not None:
			self.fields['producto'].queryset = productos

	class Meta:
		model = ItemCompra
		fields = ['nombre', 'cantidad', 'categoria', 'sucursal']

class RegistroForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']