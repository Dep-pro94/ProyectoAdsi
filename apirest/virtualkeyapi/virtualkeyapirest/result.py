#class result(object):
	#def __init__(self, **kwargs):
		#for field in ('codigo','mensaje','cambios'):
        	#setattr(self,field,kwargs.get(field,None))
        	#setattr(self,field,kwargs.get(field,None))

#results = {
   #1: result(codigo='recibido', mensaje='exitoso', cambios='exitoso'),
    #2: result(codigo='error',  mensaje='exadsfasdfsadf', cambios='exitosasdfasdf'),
#}

class  result(object):
	def __init__(self, **kwargs):
		for field in('codigo','mensaje','cambios'):
			setattr(self,field,kwargs.get(field,None))

results = {
	1: result(codigo='recibido', mensaje='exitoso',cambios='exitoifnjndjf'),
	2: result(codigo='hsdfhehf', mensaje='hola',cambios='dimelohfvbh'),
}			
	
resultok = {
	1: result(codigo='ok', mensaje='exitoso',cambios='a'),
}			
resultbad = {
	1: result(codigo='error', mensaje='fallo',cambios='no coinciden los datos con la base de datos'),
}			
resultsave = {
	1: result(codigo='ok', mensaje='registro',cambios='éxitoso'),
}			
resultnossave = {
	1: result(codigo='error', mensaje='fallo',cambios='al hacer el registro'),
}			

	
