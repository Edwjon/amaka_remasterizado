# from django.shortcuts import render, HttpResponseRedirect
# from django.http import HttpResponse, JsonResponse
# from rest_framework import permissions

# from amaka_app.models import Producto
# from amaka_app.serializers import ProductoSerializer

# from django.views.decorators.csrf import csrf_exempt


# # @csrf_exempt(['GET', ])
# # def get_data(request):
# # 	data = Producto.objects.all()
# # #	serializer_class = ProductoSerializer
# # #	permission_classes = [permissions.IsAuthenticated]

# # 	if request.method == 'GET':
# # 		#serializer = ProductoSerializer(data, many=True)
# # 		serializer = ProductoSerializer(data)
# # 		return JsonResponse(serializer.data, safe=False)


# # @csrf_exempt(['PUT', ])
# # def update_data(request):
# # 	data = Producto.objects.all()
# # #	serializer_class = ProductoSerializer
# # #	permission_classes = [permissions.IsAuthenticated]

# # 	if request.method == 'PUT':
# # 		#serializer = ProductoSerializer(data, many=True)
# # 		serializer = ProductoSerializer(data, data=request.data)
# # 		data = {}
# # 		if serializer.is_valid():
# # 			serializer.save()
# # 			data["succes"] = "update succes"
# # 			return JSONResponse(data=data)
# # 		return JsonResponse(serializer.data, safe=False)



# # @csrf_exempt(['DELETE', ])
# # def delete_data(request):
# # 	data = Producto.objects.all()
# # #	serializer_class = ProductoSerializer
# # #	permission_classes = [permissions.IsAuthenticated]

# # 	if request.method == 'DELETE':
# # 		operation = data.delete()
# # 		data = {}
# # 		if operation:
# # 			data["succes"] = "delete succes"
			

# Create your views here.
from amaka_app.models import Producto, Usuario,  Administrador, Cliente, Vendedor, Proveedor, Ingrediente, Venta, Pago
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductoSerializer, UsuarioSerializer, AdministradorSerializer, ClienteSerializer, VendedorSerializer, ProveedorSerializer, IngredienteSerializer, VentaSerializer, PagoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class AdministradorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Administrador.objects.all()
    serializer_class = AdministradorSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class VendedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProveedorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [permissions.IsAuthenticated]

class IngredienteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [permissions.IsAuthenticated]

class VentaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [permissions.IsAuthenticated]

class PagoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
    permission_classes = [permissions.IsAuthenticated]

