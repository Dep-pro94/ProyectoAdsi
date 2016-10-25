from django.contrib.auth.models import User, Group 
from virtualkeyapirest.models import  Doors
from rest_framework import serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('url','username', 'email', 'groups')
class GroupSerializer(serializers.HyperlinkedModelSerializer):			
	class Meta:
		model = Group
		fields = ('url', 'name')

class DoorsSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Doors
		fields = ('code', 'name', 'state')

class ResSerializer(serializers.Serializer):
	codigo= serializers.CharField(max_length=30)
	mensaje = serializers.CharField(max_length=30)
	cambios= serializers.CharField(max_length=30)

	def create(self, request):
		return result(codigo=error, mensaje=hola, cambios=exitosos)