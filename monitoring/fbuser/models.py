from django.db import models

# Create your models here.


class User(models.Model):

    id = models.CharField(max_length=25, unique=True)
    name = models.CharField(max_length=25, unique=True)


class Time(models.Model):

    date_t = models.DateTimeField(verbose_name=None, name=None,auto_now=False)
    user = models.ForeignKey(User)

class Contact(models.Model):

    mail = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=25, unique=True)
    user = models.ForeignKey(User,on_delete=models.PROTECT)