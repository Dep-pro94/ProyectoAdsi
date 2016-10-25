from django.db import models

class Doors(models.Model):
	code= models.IntegerField()
	name= models.CharField(max_length=30)
	state = models.CharField(max_length=30)
