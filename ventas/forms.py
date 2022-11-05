from django import forms
from clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono', 'imagen')
        labels = {
            'codigo': 'Código',
            'telefono': 'Telefono',
            'imagen': 'Imagen',
            'nombre': 'Descripcion',
        }

class EditClienteForms(forms.ModelForm):
    class Meta:
        imagen = forms.ImageField()
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono', 'imagen')
        labels = {
            'codigo': 'Código',
            'telefono': 'Telefono',
            'imagen': 'Imagen',
            'nombre': 'Descripcion',
        }

        widgets = {
            
        }