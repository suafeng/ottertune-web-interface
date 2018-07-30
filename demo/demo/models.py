#from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Config(models.Model):
  username = models.CharField(max_length=40)
  email = models.CharField(max_length=40)
  knobs_setting = models.TextField(default="")
  #throughput = models.FloatField(default=0.0)
 
class Lead(models.Model):
  username = models.CharField(max_length=20)
  tuning_time = models.FloatField(default=0.0)
  throughput = models.FloatField(default=0.0)
  rank = models.IntegerField(default=0)
  
class KnobCatalog(models.Model):
  name = models.CharField(max_length=30)
  description = models.CharField(max_length=200)
  # TO FIX, chars 
  default = models.IntegerField()
  setting = models.CharField(max_length=200)

