from django.urls import path
from .views import cliente_view, add_cliente_view, edit_cliente_view, delete_cliente_view

urlpatterns = [
    path('clientes/', cliente_view, name='Clientes'),
    path('add_cliente/', add_cliente_view, name='AddCliente'),
    path('edit_cliente/', edit_cliente_view, name='EditCliente'),
    path('delete_cliente/', delete_cliente_view, name='DeleteCliente'), 
]