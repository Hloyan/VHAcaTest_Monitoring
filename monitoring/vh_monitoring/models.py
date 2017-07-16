from django.db import models

# Create your models here.


class Urls(models.Model):

    url = models.URLField(max_length=100, db_index=True, db_column=True, unique=True)
    freq = models.BigIntegerField()
    create_time = models.DateTimeField(blank=True)
    update_time = models.DateTimeField(blank=True)


class Result(models.Model):

    monitor = models.CharField(max_length=100)
    res_time = models.DateTimeField(blank=True)
    status = models.CharField(max_length=100)
    body_size = models.PositiveIntegerField()
    run_time = models.PositiveIntegerField()
    user = models.ForeignKey(Urls)


class Action(models.Model):
    monitor = models.CharField(max_length=100)
    alert = models.CharField(max_length=100)
    user = models.ForeignKey(Urls)
