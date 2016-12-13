
from virtualkeyapirest.models import  Doors,AssignPermissions,User,Rol
from rest_framework import serializers
class DoorsSerializers(serializers.Serializer):
	class Meta:
		model  = Doors
		fields = ('idDoors', 'name', 'state','codeDoor')


class ResSerializers(serializers.Serializer):
	codigo  = serializers.CharField(max_length=30)
	mensaje = serializers.CharField(max_length=30)
	cambios = serializers.CharField(max_length=30)

	def create(self, request):
		return result(codigo=error, mensaje=hola, cambios=exitosos)

class RolSerializers(serializers.ModelSerializer):
	class Meta:
		model  = Rol
		fields = ('idRol', 'nameRol')


class UsuarioSerializers(serializers.ModelSerializer):

	class Meta:
		model  = User
		fields = ('numberDocument', 'name', 'lastName', 'username', 'password', 'email', 'rol')


class DoorReadSerializers(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Doors
		fields = ('idDoors', 'name', 'state','codeDoor','image')
	


class AssignSerializers(serializers.ModelSerializer):

	user = UsuarioSerializers(many=False, read_only=True)
	

	class Meta:
		model = AssignPermissions
		
		fields = ('idAssignPermissions', 'door', 'user', 'codeAssign','dateAssign')

###'''numberDocument''', #### 'idDoors', ################'idAssignPermissions', #############

class UsuPeSerializers(serializers.ModelSerializer):

	class Meta:
		model = User
		
		fields = ('name', 'lastName',  'rol')


class DoorsReadSerializers(serializers.ModelSerializer):
	class Meta:
		model = Doors
		fields = ('name', 'state','image')

class AssignReadSerializers(serializers.ModelSerializer):

	door = DoorsReadSerializers(many=False, read_only=True)
	user = UsuPeSerializers(many=False, read_only=True)
	

	class Meta:
		model = AssignPermissions
		
		fields = ('door', 'user','dateAssign')

class userGetSerializers(serializers.Serializer):
	numberDocument  = serializers.IntegerField()
	name = serializers.CharField(max_length=30)
	lastName = serializers.CharField(max_length=30)
	username = serializers.CharField(max_length=30)
	password = serializers.CharField(max_length=30)
	username = serializers.CharField(max_length=30)
	email = serializers.CharField(max_length=30)
	rol = serializers.CharField(max_length=30)

	def create(self, request):
		return user(numberDocument='',name='',lastName='',username='',password='',email='',rol='')
