from django.db import models

class Task(models.Model):

	name = models.CharField('Task', max_length=100)
	is_done = models.BooleanField(default=False)