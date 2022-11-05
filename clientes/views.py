from django.shortcuts import render

# Create your views here.

def cliente_view(request):
    return render(request, 'clientes/clientes.html')