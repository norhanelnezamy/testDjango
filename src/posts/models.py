from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Posts(models.Model):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z_ -]*$', 'Only alphanumeric characters are allowed.')
	title = models.CharField(max_length = 60 , validators = [alphanumeric])
	image = models.FileField(null = True , blank = True)
	content = models.TextField(max_length = 160 , validators = [alphanumeric])
	update = models.DateTimeField(auto_now = True , auto_now_add = False)
	timestamp = models.DateTimeField(auto_now = False , auto_now_add = True)

	def __unicode(self):
		return self.title

	def __str(self):
		return self.title

		