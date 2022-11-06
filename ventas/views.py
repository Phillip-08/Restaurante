from django.shortcuts import render, redirect
from app.models import Producto
from clientes.forms import AddClienteForm, EditarClienteForms
from django.contrib import messages
from .forms import AddProductoForm



# Create your views here.
def ventas_view(request):
    return render(request, 'ventas/ventas.html')

def producto_view(request):
    producto = Producto.objects.all()
    form_add_producto = AddProductoForm()
    context = {
        'producto': producto,
        'form_add_producto': form_add_producto
    }
    return render(request, 'ventas/productov.html', context)

def add_producto_view(request):
    if request.POST:
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.error(request, "Error al cargar el Producto")
                return redirect(to="Producto")
    return redirect(to="Producto")

def inventario_view(request):
    return render(request, 'ventas/inventario.html')

def add_inventario_view(request):
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.error(request, "Error al cargar el cliente")
                return redirect(to="Inventario")
    return redirect(to="Inventario")

