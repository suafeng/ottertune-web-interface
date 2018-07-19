from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

SHARED_BUFFERS_CHOICES = (('1', '3'), ('2', '9'), ('3', '27'))
EFFECTIVE_IO_CONCURRENCY_CHOICES = (('1', '1'), ('2', '2'))

class Config(models.Model):
  username = models.CharField(max_length=20)
  email = models.CharField(max_length=40)
  shared_buffers = models.IntegerField(choices=SHARED_BUFFERS_CHOICES)
  effective_io_concurrency = models.IntegerField(choices=EFFECTIVE_IO_CONCURRENCY_CHOICES)

class Lead(models.Model):
  username = models.CharField(max_length=20)
  tuning_time = models.FloatField(default=0.0)
  throughput = models.FloatField(default=0.0)
  rank = models.IntegerField(default=0)
  
class TpccForm(ModelForm):
  # def __init__(self, username, email, *args, **kwargs):
  #   self.username = user
  #   self.email = email
  #   super(TpccForm, self).__init__(*args, **kwargs)

  class Meta:
    model = Config
    fields = ['username', 'email', 'shared_buffers', 'effective_io_concurrency']