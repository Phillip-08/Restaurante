from django.shortcuts import render, redirect


# Create your views here.
def ventas_view(request):
    return render(request, 'ventas/ventas.html')

def add_cliente_view(request):
    return redirect(request, 'clientes/clientes.html')

def edit_cliente_view(request):
    return redirect(request, 'clientes/clientes.html')

def delete_cliente_view(request):
    return redirect(request, 'clientes/clientes.html')