from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from clientes.forms import AddClienteForm, EditarClienteForms
from django.contrib import messages


# Create your views here.

def cliente_view(request):
    clientes = Cliente.objects.all()
    form_personal = AddClienteForm()
    form_editar = EditarClienteForms()

    context = {
        'clientes': clientes,
        'form_personal': form_personal,
        'form_editar': form_editar,
    }
    return render(request, 'clientes/clientes.html', context)

def add_cliente_view(request):
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages.error(request, "Error al cargar el cliente")
                return redirect(to="Clientes")
    return redirect(to="Clientes")

def edit_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form = EditarClienteForms(
            request.POST, request.FILES, instance= cliente)
        if form.is_valid:
            form.save()
    return redirect(to="Clientes")

def delete_cliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_eliminar'))
        cliente.delete()
    return redirect(to="Clientes")