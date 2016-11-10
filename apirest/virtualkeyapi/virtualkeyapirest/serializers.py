# from django.contrib.auth.models import User, Group
from virtualkeyapirest.models import  Doors,AssignPermissions,User,Rol
from rest_framework import serializers
# class UserSerializer(serializers.HyperlinkedModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ('url','username', 'email', 'groups')
# class GroupSerializer(serializers.HyperlinkedModelSerializer):			
# 	class Meta:
# 		model = Group
# 		fields = ('url', 'name')

class DoorsSerializers(serializers.Serializer):
	class Meta:
		model = Doors
		fields = ('idDoors', 'name', 'state','codeDoor')


class ResSerializers(serializers.Serializer):
	codigo= serializers.CharField(max_length=30)
	mensaje = serializers.CharField(max_length=30)
	cambios= serializers.CharField(max_length=30)

	def create(self, request):
		return result(codigo=error, mensaje=hola, cambios=exitosos)

class RolSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Rol
		fields = ('idRol', 'nameRol')


class UsuarioSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('numberDocument', 'name', 'lastName', 'username', 'password', 'email', 'idrol')
		

class AsignarSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = AssignPermissions
		fields = ('idAssignPermissions', 'door', 'user', 'codeAssign')

class DoorReadSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Doors
		fields = ('idDoors', 'name', 'state','codeDoor','image')
	