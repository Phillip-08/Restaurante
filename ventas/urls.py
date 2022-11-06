from django.urls import path, include
from .views import ventas_view, inventario_view, producto_view

urlpatterns = [
    path('ventas/', ventas_view, name='Ventas'), 
    path('inventario/', inventario_view, name='Inventario'),
    path('producto/', producto_view, name='Producto'),
    path('add_producto/', producto_view, name='AddProducto'),
]