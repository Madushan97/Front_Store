import email
from turtle import title
from django.db import models

# Create your models here.

class Product(models.Model):

    # primary key
    # sku = models.CharField(max_length=10, primary_key=True)

    title = models.CharField(max_length=255)
    description = models.TextField()
    # max price = 999999.99
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)


class Customer(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_day = models.DateField(null=True)