from rest_framework import serializers
from amaka_app.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre', 'costo', 'ingrediente', 'cantidad', 'imagen', 'tamano', 'vendedor')