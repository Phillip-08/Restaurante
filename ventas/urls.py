from django.urls import path, include
from .views import ventas_view, add_cliente_view, edit_cliente_view, delete_cliente_view

urlpatterns = [
    path('ventas/', ventas_view, name='Ventas'), 
    path('add_cliente/', add_cliente_view, name='AddCliente'),
    path('edit_cliente/', edit_cliente_view, name='EditCliente'),
    path('delete_cliente/', delete_cliente_view, name='DeleteCliente')
]