from django.db import models

class Doors(models.Model):
	idDoors = models.AutoField(primary_key=True)
	name 	= models.CharField(max_length=45, unique=True)
	state 	= models.IntegerField()
	codeDoor= models.CharField(max_length=45 , unique=True, null=True)
	image 	= models.TextField()

class Rol(models.Model):
	idRol 	= models.AutoField(primary_key=True)
	nameRol = models.CharField(max_length=45)

class User(models.Model):
	numberDocument = models.IntegerField(primary_key=True)	
	name 		   = models.CharField(max_length=45)
	lastName 	   = models.CharField(max_length=45)
	username 	   = models.CharField(max_length=45, unique= True)
	password 	   = models.CharField(max_length=45,)
	email 		   = models.EmailField(max_length=75, unique=True)
	rol 		   = models.ForeignKey(Rol)


class AssignPermissions(models.Model):
	idAssignPermissions = models.AutoField(primary_key=True)
	door 				= models.ForeignKey(Doors)
	user 				= models.ForeignKey(User)
	codeAssign			= models.CharField(max_length=45, unique=True)
	dateAssign			= models.DateTimeField(auto_now=True)
