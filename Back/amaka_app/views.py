from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from rest_framework import permissions

from amaka_app.models import Producto
from amaka_app.serializers import ProductoSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
	data = Producto.objects.all()
	serializer_class = ProductoSerializer
	permission_classes = [permissions.IsAuthenticated]



	# if request.method == 'GET':
	# 	serializer = ProductoSerializer(data, many=True)
	# 	return JsonResponse(serializer.data, safe=False)
