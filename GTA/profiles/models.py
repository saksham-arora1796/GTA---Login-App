from django.db import models

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(default='description default text')
#For my own notes : Saksham Arora
#	location = models.CharField(max_length=120, default='My location default', blank=True, null=True)
#	job = models.CharField(max_length=120, default='My job default')

	def __str__(self):
		return self.name