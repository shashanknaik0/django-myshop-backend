from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=False)
    price = models.IntegerField(null=False)
    quantity = models.CharField(max_length=20,null=False)
    imgURL= models.CharField(max_length=255,null=False)
    description = models.CharField(max_length=100,null=False)
