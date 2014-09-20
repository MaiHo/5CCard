from django.db import models

# Create your models here.

class Flex(models.Model):
	balance = models.FloatField() #how much flex they have
	transaction = models.TextField() #date/time, location and amount used at transaction

class NumMeals(models.Model):
	mealBalance = models.FloatField() #meals they have left
	activity = models.TextField() #where they spent their meal, what time, what class

class CCash(models.Model):
	balance = models.FloatField() #how much claremont cash they have 
	transaction = models.TextField() #date/time, location and amount used at cCash trasaction

class User(models.Model):
	user_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	flex = models.OneToOneField(Flex) #'how much they have in flex'
	numMeals = models.OneToOneField(NumMeals) #'how many meals they have left'
	cCash = models.OneToOneField(CCash) #'how much claremont cash they have left'

