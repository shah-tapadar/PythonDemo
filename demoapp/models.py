from django.db import models

class Data(models.Model):
	name = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	email = models.CharField(max_length=50)