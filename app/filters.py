import django_filters
from .models import *

class ProductoFilter(django_filters.FilterSet):

    class Meta:
        model = Producto
        fields = [
            'categoria',
        ]