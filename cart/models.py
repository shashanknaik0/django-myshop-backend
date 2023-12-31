from django.db import models
from django.contrib.auth.models import User
from product.models import Product

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(to=User,on_delete=models.CASCADE)
    product_id = models.ForeignKey(to=Product,on_delete=models.CASCADE)
