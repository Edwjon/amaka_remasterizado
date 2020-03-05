# from django.db import models


# class ExampleModel(models.Model):
# 	firstname = models.CharField(max_length=200)
# 	lastname = models.CharField(max_length=200)


# class Producto(models.Model):
#     nombre = models.CharField(max_length=50)
#     costo = models.IntegerField()
#     ingrediente = models.ManyToManyField("Ingrediente")
#     cantidad = models.IntegerField()
#     imagen = models.TextField()
#     tamano = models.TextField()
#     categoria = models.ForeignKey("Categoria", on_delete=models.CASCADE)
#     vendedor = models.ManyToManyField("Vendedor")
#     def __str__(self):
#         return self.nombre
    

# class Usuario(models.Model):
#     contrasena = models.CharField(max_length=20)
#     email = models.EmailField(max_length=254)
#     fecha_de_nacimiento = models.DateField(auto_now=False, auto_now_add=False) 
#     #rol = models.ForeignKey("Rol", on_delete=models.CASCADE)
#     #carrito = models.ManyToManyField("Carrito")
#     #transacciones = models.ManyToManyField("Transaccion")
#     def __str__(self):
#         return self

# class Nombre(models.Model):
#     nombre = models.CharField(max_length=50)
#     usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
#     def __str__(self):
#         return self.nombre

# class Apellido(models.Model):
#     apellido = models.CharField(max_length=50)
#     usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
#     def __str__(self):
#         return self.apellido

# class Vendedor(models.Model):
#     nombre = models.CharField(max_length=50)
#     apellido = models.CharField(max_length=50)
#     telefono = models.CharField(max_length=11)  
#     proveedor = models.ForeignKey("Proveedor", on_delete=models.CASCADE)
#     def __str__(self):
#         return self.nombre

# class Proveedor(models.Model):
#     nombre = models.CharField(max_length=50)    
#     def __str__(self):
#         return self.nombre

# #class Carrito(models.Model):
# #    productos = models.ManyToManyField("Producto")
# #    cantidad = models.IntegerField()
# #    def __str__(self):
# #        return str(self.productos.nombre)

# class Ingrediente(models.Model):
#     nombre = models.CharField(max_length=50)
#     def __str__(self):
#         return self.nombre

# class Venta(models.Model):
#     productos_comprados = models.ManyToManyField("Producto")
#     def __str__(self):
#         return 

# class Pago(models.Model):
#     metodo_de_pago = models.CharField( max_length=50)
#     venta = models.ForeignKey("Venta", on_delete=models.CASCADE)
#     fecha = models.DateField(auto_now=False, auto_now_add=True)
#     def __str__(self):
#         return

from django.db import models

# Create your models here.


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.IntegerField()
    ingrediente = models.ManyToManyField("Ingrediente")
    cantidad = models.IntegerField()
    imagen = models.TextField()
    tamano = models.TextField()
    vendedor = models.ManyToManyField("Vendedor")
    def _str_(self):
        return self.nombre
    

class Usuario(models.Model):
    contrasena = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    fecha_de_nacimiento = models.DateField(auto_now=False, auto_now_add=False) 
    def _str_(self):
        return self.nombre

class Administrador(models.Model):
    usuario = models.OneToOneField("Usuario", on_delete=models.CASCADE)
    def _str_(self):
        return str(self.usuario)

class Cliente(models.Model):
    usuario = models.OneToOneField("Usuario", on_delete=models.CASCADE)
    def _str_(self):
        return str(self.usuario)

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)  
    proveedor = models.ForeignKey("Proveedor", on_delete=models.CASCADE)
    def _str_(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    def _str_(self):
        return self.nombre

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)
    def _str_(self):
        return self.nombre

class Venta(models.Model):
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    isPago = models.BooleanField()
    productos_comprados = models.ManyToManyField("Producto")
    def _str_(self):
        return str(self.cliente)

class Pago(models.Model):
    metodo_de_pago = models.CharField( max_length=50)
    venta = models.ForeignKey("Venta", on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=True)
    def _str_(self):
        return str(self.venta)