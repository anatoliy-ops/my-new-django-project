from django.db import models,migrations
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
class Order(models.Model):
    datetime = models.DateTimeField()