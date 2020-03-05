from django.db import models

# Create your models here.


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
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
    id = models.AutoField(primary_key=True)
    contrasena = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    fecha_de_nacimiento = models.DateField(auto_now=False, auto_now_add=False) 
    def _str_(self):
        return self.nombre

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField("Usuario", on_delete=models.CASCADE)
    def _str_(self):
        return str(self.usuario)

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField("Usuario", on_delete=models.CASCADE)
    def _str_(self):
        return str(self.usuario)

class Vendedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=11)  
    proveedor = models.ForeignKey("Proveedor", on_delete=models.CASCADE)
    def _str_(self):
        return self.nombre

class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def _str_(self):
        return self.nombre

class Ingrediente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    def _str_(self):
        return self.nombre

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    isPago = models.BooleanField()
    productos_comprados = models.ManyToManyField("Producto")
    def _str_(self):
        return str(self.cliente)

class Pago(models.Model):
    id = models.AutoField(primary_key=True)
    metodo_de_pago = models.CharField( max_length=50)
    venta = models.ForeignKey("Venta", on_delete=models.CASCADE)
    fecha = models.DateField(auto_now=False, auto_now_add=True)
    def _str_(self):
        return str(self.venta)