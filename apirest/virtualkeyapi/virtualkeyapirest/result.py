
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
resultdoor = {
	1: result(codigo='ok', mensaje='puerta',cambios='estado'),
}			
			
resultGetData = {
	1: result(codigo='ok', mensaje='valores',cambios='obtenidos'),
}

resultNoGetData = {
	1: result(codigo='error', mensaje='valores',cambios='invalidos'),
}

resultOpen = {
	1: result(codigo='ok', mensaje='Puerta',cambios='abierta'),
}
resultClosed = {
	1: result(codigo='ok', mensaje='Puerta',cambios='cerrada'),
}

resultError = {
	1: result(codigo='error', mensaje='valores',cambios='invalidos'),
}
resultDoorNoExist = {
	1: result(codigo='error', mensaje='Puerta',cambios='No existe'),
}

resultUpdateUser = {
	1: result(codigo='ok', mensaje='User',cambios='updated'),
}

resultSaveAssign = {
	1: result(codigo='ok', mensaje='datos',cambios='guardados'),
}
ok = {
	1: result(codigo='ok', mensaje='ok',cambios='ok'),
}
no = {
	1: result(codigo='no', mensaje='no',cambios='no'),
}
resultCorreoEncontrado={
	1: result(codigo='ok', mensaje='correo enviado con',cambios='exito'),
}
resultCorreoNoEncontrado={
	1: result(codigo='error', mensaje='correo',cambios='no encontrado'),
}
resultAdmin={
	1: result(codigo='el', mensaje='rol es',cambios='administrador'),
}
resultInstructor={
	1: result(codigo='el', mensaje='rol es',cambios='instructor'),
}
resultAprendiz={
	1: result(codigo='el', mensaje='rol es',cambios='aprendiz'),
}



