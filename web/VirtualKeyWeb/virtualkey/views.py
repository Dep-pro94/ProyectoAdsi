import urllib.request
import json

from django.shortcuts import render

# Create your views here.
def index(request):
	
	#door = urllib.request.urlopen("https://gist.githubusercontent.com/mdtr000/37ae4679b585d39d0f784d95d08794ce/raw/18fe5486f740e55995c38970feb622898d5358d5/prueba").read().decode('utf8')
	door = urllib.request.urlopen("https://gist.githubusercontent.com/mdtr000/37ae4679b585d39d0f784d95d08794ce/raw/1519d0b8958efd625900e3caeb8a2ddd3b655321/prueba").read().decode('utf8')	
	decoded = json.loads(door)
	
	#puerta1 = str(decoded["Puertas"][0]["Name"])
	#print ("Ambiente "+puerta1+" State "+puerta1s)
	doors=[];
	for x in decoded["Puertas"]:
		name = str(x["Name"])
		state = x["state"]
		image = str(x["image"])		
		print ("Ambiente "+ name )
		statew=' '
		if state==0 :
			statew='CERRADO'
		else:
			statew='ABIERTO'	

		door_={ 'name':name,'state':statew, 'image':image }
		doors.append(door_)

	return render(request, 'virtualkey/index.html',{
			'doors':doors
		})