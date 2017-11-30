from django.db import models

# Create your models here.


class UserData(models.Model):
    user_name = models.CharField('user_name', max_length=200,blank=True, null=True)
    brain_signal = models.CharField('brain_signal', blank=True, null=True)
