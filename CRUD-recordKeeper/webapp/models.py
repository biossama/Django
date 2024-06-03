from django.db import models

# Create your models here.

class Record(models.Model):

	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	date_time = models.DateTimeField(auto_now_add=True)
	email = models.EmailField(max_length=254, unique=True)
	phone = models.CharField(max_length=20)
	adress = models.CharField(max_length=300)
	city = models.CharField(max_length=100)
	province = models.CharField(max_length=150)
	country = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural = "Record"

	def __str__(self):
		return self.first_name + " " + self.last_name
