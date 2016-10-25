#from django.shortcuts import render
from django.contrib.auth.models import User, Group
from virtualkeyapirest.models import  Doors
from rest_framework import viewsets
from virtualkeyapirest.serializers import UserSerializer, GroupSerializer, DoorsSerializers, ResSerializer
from virtualkeyapirest.result import *
import requests

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all().order_by('date_joined')
	serializer_class = UserSerializer
class GroupViewSet (viewsets.ModelViewSet):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer	

class DoorsViewSet(viewsets.ModelViewSet):
	queryset = Doors.objects.all()
	serializer_class = DoorsSerializers

#class UserViewSet(viewsets.Viewsets):
	#def create(self, request):
		#pass

class ResViewSet(viewsets.ViewSet):
    serializer_class = ResSerializer

    #def create(self, request):
        #serializer = serializers.ResSerializer(
        	#instance=result.values(), many=true)
        #return Response(serializer.data)

    def create(self, request):
        serializer = ResSerializer(
            instance=results.values(), many=True)
        return Response(serializer.data)    

