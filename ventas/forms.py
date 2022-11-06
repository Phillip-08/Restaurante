from django import forms
from app.models import Producto

class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio','descripcion','imagen','categoria')
        labels = {
            'nombre': 'Nombre cliente:',
            'precio': 'Precio:',
            'descripcion':'Descripcion del Producto:',
            'imagen': 'Imagen del Producto:',
            'categoria': 'Categoria',
        }