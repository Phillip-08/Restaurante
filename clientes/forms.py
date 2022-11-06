from django import forms
from clientes.models import Cliente


class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Código cliente:',
            'nombre': 'Nombre cliente:',
            'telefono': 'Telefono: (Contacto):'

        }

class EditarClienteForms(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Código cliente:',
            'nombre': 'Nombre cliente:',
            'telefono': 'Telefono: (Contacto):'

        }
        widgets = {
            'codigo': forms.TextInput(attrs={'type': 'text', 'id': 'codigo_editar'}),
            'nombre': forms.TextInput(attrs={'id': 'nombre_editar'}),
            'telefono': forms.TextInput(attrs={'id': 'telefono_editar'}),
        }