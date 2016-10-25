import urllib.request
import json

from django.shortcuts import render

# Create your views here.
def index(request):
	
	#door = urllib.request.urlopen("https://gist.githubusercontent.com/anonymous/f19953c3a9f9d7c7561c12e13ca01034/raw/be090257579863c1b4ccd6e76206c02d312a8733/prueba").read().decode('utf8')
	door = urllib.request.urlopen("https://gist.githubusercontent.com/mdtr000/1046e2120c54ed4ae68a26bab783cfc5/raw/4920d8819676861863b981f35b021be87720b56e/prueba").read().decode('utf8')
	#door=str(door)
	#print(str(door))
		#decoded = json.loads(' {"hola":"aaaaaaaaaa"}' )
		#fruta =decoded["hola"]

	decoded = json.loads(door)
	#fruta = str(decoded["Fruteria"][0]["Fruta"][0]["Nombre"])
	puerta1 = str(decoded["Estado"][0]["Name"])
	puerta1s = str(decoded["Estado"][0]["state"])

	puerta2 = str(decoded["Estado"][1]["Name"])
	puerta2s = str(decoded["Estado"][1]["state"])

	puerta3 = str(decoded["Estado"][2]["Name"])
	puerta3s = str(decoded["Estado"][2]["state"])

	print ("Ambiente "+puerta1+" State "+puerta1s)
	print ("Ambiente "+puerta2+" State "+puerta2s)
	print ("Ambiente "+puerta3+" State "+puerta3s)
	#print (decoded)

	return render(request, 'virtualkey/index.html')