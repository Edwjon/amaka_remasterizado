from rest_framework import serializers
from amaka_app.models import Producto, Usuario, Administrador, Cliente, Vendedor, Proveedor, Ingrediente, Venta, Pago

class ProductoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'costo', 'cantidad', 'imagen', 'tamano', 'ingrediente']

class UsuarioSerializer (serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'contrasena', 'nombre', 'apellido', 'email', 'fecha_de_nacimiento']

class AdministradorSerializer (serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = ['id', 'usuario']        

class ClienteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '_all_'

class VendedorSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Vendedor
        fields = ['id', 'nombre', 'apellido', 'telefono', 'proveedor']

class ProveedorSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Proveedor
        fields = ['id', 'nombre']

class IngredienteSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Ingrediente
        fields = ['id', 'nombre']

class VentaSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Venta
        fields = ['id', 'cliente', 'isPago', 'productos_comprados']

class PagoSerializer (serializers.ModelSerializer):
    class Meta: 
        model = Vendedor
        fields = ['id', 'metodo_de_pago', 'venta', 'fecha']