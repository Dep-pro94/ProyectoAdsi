"""virtualkeyapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import  include, url
from rest_framework import routers
from virtualkeyapirest import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'api/doors', views.DoorsViewSet,base_name='api')
router.register(r'result', views.ResultViewSet, base_name='results')
router.register(r'user', views.UsuarioViewSet,base_name='user')
router.register(r'api/login', views.LoginViewSet,base_name='api')
router.register(r'api/register', views.saveUserViewSet,base_name='api')
router.register(r'api/read', views.readDoorsViewSet,base_name='api')
# router.register(r'AssignPermissions', views.AsignarViewSet,base_name='Asignar')

urlpatterns = [
url(r'^', include(router.urls)),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
url(r'^admin/', include(admin.site.urls)),
]

