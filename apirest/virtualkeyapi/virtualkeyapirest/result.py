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
	
	
