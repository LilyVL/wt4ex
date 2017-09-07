from django.db import models
from mongoengine import *	

# Create your models here.
class Recipe(models.Model):
	name = StringField(max_length=200)
	ingredients = StringField()
	calories = IntField()
	prep_time = IntField()

	def __str__(self):
		return self.name

