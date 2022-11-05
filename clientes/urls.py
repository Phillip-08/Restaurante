from django.urls import path
from .views import cliente_view

urlpatterns = [
    path('clientes/', cliente_view, name='Clientes'), 
]