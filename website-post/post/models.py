from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	slug = models.SlugField()
	date = models.DateTimeField(auto_now_add=True)
	banner = models.ImageField(default="backup.png", blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE, default=True )

	class Meta:
		verbose_name_plural = 'Post'

	def __str__(self):
		return self.title


