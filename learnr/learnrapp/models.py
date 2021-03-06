from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
	sender = models.ForeignKey(User)
	text = models.CharField(max_length=400)
	time = models.DateTimeField()

	def user(self):
		return User.objects.get(pk=self.user_id)

class Problem(models.Model):
	author = models.ForeignKey(User)
	problem_text = models.CharField(max_length=600)
	category = models.CharField(max_length=30)

class PublicUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=4000, null=True)
    output = models.CharField(max_length=4000, null=True)
    last_watched = models.DateTimeField()