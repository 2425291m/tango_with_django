from django.db import models

# Create your models here.
class Category(models.Model):
	name=models.CharField(max_length=128, unique=True)

	#may be able to remove 'self' due to Python version being > 3.0
	def __str__(self):
		return self.name

class Page(models.Model):
	category=models.ForeignKey(Category)
	title=models.CharField(max_length=128)
	url=models.URLField()
	views=models.IntegerField(default=0)

	def __str__(self):
		return self.title