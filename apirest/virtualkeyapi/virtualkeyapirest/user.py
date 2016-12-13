
class  user(object):
	def __init__(self, **kwargs):
		for field in('numberDocument','name','lastName','username','password','email','rol'):
			setattr(self,field,kwargs.get(field,None))
			
'''
user = {
	1: objectUsuario(numberDocument='',name='',lastName='',username='',password='',email='',rol=''),
	
}		
'''