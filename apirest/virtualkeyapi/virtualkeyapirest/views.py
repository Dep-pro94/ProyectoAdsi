import urllib.request
import smtplib
from virtualkeyapirest.models import  Doors , User, Rol, AssignPermissions
from rest_framework import viewsets
from virtualkeyapirest.serializers import  DoorsSerializers,ResSerializers,DoorReadSerializers,UsuarioSerializers,AssignReadSerializers,RolSerializers,userGetSerializers
from virtualkeyapirest.result import *
from virtualkeyapirest.user import *
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.conf import settings
from email import encoders
from email.mime.text import MIMEText


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
		user= request.data['user']
		password= request.data['pass']

		try:
			userobject=User.objects.get(username=user, password=password)
			
			if(userobject!=None):
				userObject = User.objects.get(username__exact = user)
				validarRol=userobject.rol.idRol
				
				if(validarRol==1):
					serializer = ResSerializers(instance=resultAdmin.values(), many=True)
					return Response(serializer.data)

				elif(validarRol==2):
					serializer = ResSerializers(instance=resultInstructor.values(), many=True)
					return Response(serializer.data)

				else:
					serializer = ResSerializers(instance=resultAprendiz.values(), many=True)
					return Response(serializer.data)

		except ObjectDoesNotExist:
			serializer = ResSerializers(instance=resultbad.values(), many=True)
			return Response(serializer.data)

class saveUserViewSet(viewsets.ViewSet):
	serializer_class=ResSerializers

	def create(self,request):

		number=request.data['number']
		name=request.data['name']
		last=request.data['last']
		user=request.data['user']
		password=request.data['password']
		email=request.data['email']
		# idRol=request.data['idRol']
		
		

		# rol=Rol.objects.get(idRol=idRol)
		rol=Rol.objects.get(idRol='3')
		nombreRol=rol.nameRol
		
		print(nombreRol)
		
		# u =User(numberDocument=number,name=name,lastName=last, username=user, password=password, email=email,rol=rol)
		u =User(numberDocument=number,name=name,lastName=last, username=user,password=password, email=email,rol=rol)
		# u.password=hash_password(password)
		u.save()
	  
		#r.save()
		serializer = ResSerializers(instance=resultsave.values(), many=True)
		return Response(serializer.data)
		

class readDoorsViewSet(viewsets.ModelViewSet):
	queryset = Doors.objects.all()
	num=Doors.objects.count()
	print("numero de objetos", num)
	serializer_class=DoorReadSerializers

class doorPostViewSet(viewsets.ViewSet):
	serializer_class = ResSerializers

	def create(self, request):

		name=request.POST.get['name','']
		codeDoor=request.POST.get['code','']
		image=request.POST.get['image','']
		state=request.POST.get['state','']

		d =Doors(name=name, codeDoor= code, image=image, state=state)
		d.save()
		print("datos##########################  ",request.data)
		serializer = ResSerializers(instance=resultdoor.values(), many=True)
		return Response(serializer.data)


class doorSave(viewsets.ViewSet):
	serializer_class=ResSerializers

	def create(self,request):

		name=request.data['name']
		state=request.data['state']
		codeDoor=request.data['code']
		image=request.data['image']
		
		print(name)
		print(codeDoor)
		print(codeDoor)
		print(image)
		
		do = Doors(name=name,state=state, codeDoor=codeDoor, image=image)
		do.save()
	  
		serializer = ResSerializers(instance=resultdoor.values(), many=True)
		return Response(serializer.data)
		

class doorChangeValue(viewsets.ViewSet):
	serializer_class = ResSerializers

	def create(self, request):
		idDoor= request.data['idDoor']
		state= request.data['state']
		idUser=request.data['idUser']
		codeAssign=request.data['code']

		print(idDoor)
		print(state)
		print(idUser)
		print(codeAssign)

		assingObject=AssignPermissions.objects.filter(codeAssign=codeAssign).count()
		if (assingObject>0):
			return self.validar(idDoor,state)		
			
		else:

			door=Doors.objects.get(idDoors=idDoor)
			user=User.objects.get(numberDocument=idUser)
			asig=AssignPermissions.objects.create(door=door, user=user,codeAssign=codeAssign)
			asig.save()
		
			return self.validar(idDoor,state)


	def validar(self,idDoor,state):

		if(idDoor != None and state != None):
			
			
			if(int (idDoor)==1):
				print(idDoor)
				pin='12'
				return self.cambiar(pin,state,idDoor)
				

			elif(int (idDoor)==2) :
				pin='11'
				return self.cambiar(pin,state,idDoor)

			else:
				serializer=ResSerializers(instance=resultError.values(), many=True)
				return Response(serializer.data)

		else:
			serializer=ResSerializers(instance=resultNoGetData.values(), many=True)
			return Response(serializer.data)

	def cambiar(self, pin,state,idDoor):
	
		server="http://192.168.43.110/arduino/doors/"
		responseYun = urllib.request.urlopen(server+pin+'/'+state).read().decode('utf8')
		print("Este es el valor de retorno del Yun..................")
		print(responseYun)

		if(responseYun=="abierto"):
			door = Doors.objects.filter(idDoors=idDoor)
			door.update(state = state )
			serializer=ResSerializers(instance=resultOpen.values(), many=True)
			return Response(serializer.data)


		elif (responseYun=="cerrado"):
			door = Doors.objects.filter(idDoors=idDoor)
			door.update(state = state )
			serializer=ResSerializers(instance=resultClosed.values(), many=True)
			return Response(serializer.data)

		else:
			serializer=ResSerializers(instance=resultError.values(), many=True)
			return Response(serializer.data)
					

class updateUserViewSet(viewsets.ViewSet):
	serializer_class=ResSerializers

	def create(self,request):

		number=request.data['number']
		name=request.data['name']
		last=request.data['last']
		user=request.data['username']
		password=request.data['password']
		email=request.data['email']
		print (number)
		print (name)
		print (number)
		print (last)
		print (user)
		print (password)
		print (number)
		
		use = User.objects.filter(numberDocument=number)
		use.update(name = name , lastName=last , username=user, password=password, email=email)
		serializer=ResSerializers(instance=resultUpdateUser.values(), many=True)
		return Response(serializer.data)


class readUserViewSet(viewsets.ModelViewSet):
	
	queryset = User.objects.all()
	serializer_class=UsuarioSerializers
 

class readAssingViewSet(viewsets.ModelViewSet):
	
	queryset = AssignPermissions.objects.all()
	query=AssignPermissions.objects.count()
	# print(queryset)
	serializer_class=AssignReadSerializers


class readRolViewSet(viewsets.ModelViewSet):
	
	queryset = Rol.objects.all()
	

 	

class updatePassViewSet(viewsets.ViewSet):

	EMAIL_USE_TLS = True
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_PORT = 465
	EMAIL_HOST_USER = 'virtualkeysena@gmail.com'
	EMAIL_HOST_PASSWORD = 'virtualsenakey'


	serializer_class=UsuarioSerializers

	def create(self,request):

		email=request.data['email']

		print(type(str(email)))

		try:
			userobject=User.objects.get(email =email)
			if(userobject!=None):


				user = User.objects.get(email__iexact = email)
				password=user.password	
				emailDirigido=user.email
				print(emailDirigido)
				print(password)

				origen = 'virtualkeysena@gmail.com'
				passw = "virtualsenakey"
				

				smt = smtplib.SMTP('smtp.gmail.com', 587)
				smt.ehlo()
				smt.starttls()
				smt.login(origen,passw)
				asunto="Recuperación de contraseña"
				desde=origen
				contenido="Su contraseña es : "+password
				mensaje=MIMEText(contenido)
				mensaje['Subject']=asunto
				mensaje['From']=desde
				mensaje['To']=emailDirigido
				smt.sendmail(desde, emailDirigido, mensaje.as_string())
				print ("Listooo!!")
				smt.close()

				
				
				serializer=ResSerializers(instance=resultCorreoEncontrado.values(), many=True)
				return Response(serializer.data)
		except ObjectDoesNotExist:
			serializer = ResSerializers(instance=resultCorreoNoEncontrado.values(), many=True)
			return Response(serializer.data)



class getUserViewSet(viewsets.ModelViewSet):
	
	def create(self,request):
		
		username=request.data['username']	
		userObject = User.objects.get(username__exact = username)
				
		userData={
			1: user(numberDocument=userObject.numberDocument,name=userObject.name,lastName=userObject.lastName,username=userObject.username,password=userObject.password,email=userObject.email,rol=userObject.rol.nameRol),
		}		

		serializer=userGetSerializers(instance=userData.values(),many=True)
		return Response(serializer.data)


class readLimitViewSet(viewsets.ModelViewSet):
	
	queryset=AssignPermissions.objects.all().order_by('idAssignPermissions')[:2]
	serializer_class=AssignReadSerializers

