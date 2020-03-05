"""amaka_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.conf.urls import url
# from django.contrib import admin
# from django.views.generic.base import TemplateView
# from amaka_app.views import *

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^getData/', get_data),
#     url(r'^.*', TemplateView.as_view(template_name="home.html"), name="home")
# ]

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from amaka_app import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'administradores', views.AdministradorViewSet)
router.register(r'clientes', views.ClienteViewSet)
router.register(r'vendedores', views.VendedorViewSet)
router.register(r'proveedores', views.ProveedorViewSet)
router.register(r'ingredientes', views.IngredienteViewSet)
router.register(r'ventas', views.VentaViewSet)
router.register(r'pagos', views.PagoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]