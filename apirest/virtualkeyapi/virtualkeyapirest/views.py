#from django.shortcuts import render
#from django.contrib.auth.models import User, Group,
from virtualkeyapirest.models import  Doors , User, Rol, AssignPermissions
from rest_framework import viewsets
from virtualkeyapirest.serializers import  DoorsSerializers,ResSerializers,DoorReadSerializers
from virtualkeyapirest.result import *
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist




class DoorsViewSet(viewsets.ModelViewSet):
	queryset=Doors.objects.all()
	serializer_class=DoorsSerializers

class ResultViewSet(viewsets.ViewSet):
	serializer_class=ResSerializers

	def list(self,request):
		#serializer=ResSerializers
		serializer = ResSerializers(instance=results.values(), many=True)
		return Response(serializer.data)

class UsuarioViewSet(viewsets.ModelViewSet):
	serializer_class=ResSerializers
	
	def create(self,request):

		print(request)
		serializer=ResSerializers

class LoginViewSet(viewsets.ViewSet):
	serializer_class = ResSerializers

	def create(self, request):
		print("datos##########################  ",request.data)
		user= request.data['user']
		password= request.data['pass']
		try:
			userobject=User.objects.get(username=user, password=password)
			if(userobject!=None):
				serializer = ResSerializers(instance=resultok.values(), many=True)
				return Response(serializer.data)
		except ObjectDoesNotExist:
			serializer = ResSerializers(instance=resultbad.values(), many=True)
			return Response(serializer.data)

		#Coger el user y password y llamar la consulta al User.get o User.filter

class saveUserViewSet(viewsets.ViewSet):
	serializer_class=ResSerializers

	def create(self,request):


		number=request.data['number']
		name=request.data['name']
		last=request.data['last']
		user=request.data['user']
		password=request.data['password']
		email=request.data['email']
		idRol=request.data['idRol']
		print(number)
		print(name)
		print(last)
		print(user)
		print(password)
		print(email)
		print(idRol)
		#r=Rol(idRol=idRol)
		rol=Rol.objects.get(idRol=idRol)
		u =User(numberDocument=number,name=name,lastName=last, username=user, password=password, email=email,rol=rol)
		u.save()
	  
		#r.save()
		serializer = ResSerializers(instance=resultsave.values(), many=True)
		return Response(serializer.data)
		

class readDoorsViewSet(viewsets.ModelViewSet):
	queryset = Doors.objects.all()
	num=Doors.objects.count()
	print("numero de objetos", num)
	serializer_class=DoorReadSerializers


	
	
	

        