from django.db import models

class Urls (models.Model):
	original = models.CharField (max_length=32)
	short = models.CharField (max_length=32)

