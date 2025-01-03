from django.db import models


class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50)
	quality =  models.CharField(max_length=50)
	weapon =  models.CharField(max_length=100)
	element = models.CharField(max_length=15)
	region =  models.CharField(max_length=100)
	

	def __str__(self):
		return(f"{self.name}")