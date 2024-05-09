from django import forms
from .models import Sucursal, ItemCompra, ItemProveedor
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
        fields = ['sucursal', 'producto', 'proveedor', 'unidades', 'minimo_unidades', 'costo', 'cantidad', 'costo_total'] 
        widgets = {
            'sucursal': forms.TextInput(attrs={'type': 'text'}),
            'producto': forms.TextInput(attrs={'type': 'text'}),
            'unidades': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'minimo_unidades': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'costo': forms.NumberInput(attrs={'readonly': 'readonly'}),
            'proveedor': forms.TextInput(attrs={'readonly': 'readonly'}),
            'cantidad': forms.NumberInput(attrs={'step': '1', 'readonly': 'readonly'}),
            'costo_total': forms.NumberInput(attrs={'readonly': 'readonly'})
        }

class RegistroForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']