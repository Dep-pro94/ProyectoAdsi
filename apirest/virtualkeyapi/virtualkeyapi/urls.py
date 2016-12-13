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
router.register(r'api/doors', views.DoorsViewSet,base_name='api/doors')
router.register(r'result', views.ResultViewSet, base_name='results')
router.register(r'api/login', views.LoginViewSet,base_name='api/login')
router.register(r'api/register', views.saveUserViewSet,base_name='api/register')
router.register(r'api/read', views.readDoorsViewSet,base_name='api/read')
router.register(r'api/doorPost', views.doorPostViewSet,base_name='api/doorPost')
router.register(r'api/changeValue', views.doorChangeValue,base_name='api/changeValue')
router.register(r'api/doorSave', views.doorSave,base_name='api/doorSave')
router.register(r'api/readUser', views.readUserViewSet,base_name='api/readUser')
router.register(r'api/readDoorUp', views.readAssingViewSet,base_name='api/readDoorUp')
router.register(r'api/readRol', views.readRolViewSet,base_name='api/readRol')
# router.register(r'api/validateEmail', views.validateEmailViewSet,base_name='api/validateEmail')
router.register(r'api/updatePass', views.updatePassViewSet,base_name='api/updatePass')
router.register(r'api/getUser', views.getUserViewSet,base_name='api/getUser')
router.register(r'api/readLimit', views.readLimitViewSet,base_name='api/readLimit')


# router.register(r'api/updateUser', views.updateUserViewSet,base_name='api')
# router.register(r'AssignPermissions', views.AsignarViewSet,base_name='Asignar')

urlpatterns = [
url(r'^', include(router.urls)),
url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
url(r'^admin/', include(admin.site.urls)),
]

