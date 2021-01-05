from django.db import models

# Create your models here.
class ShopItem(models.Model):
    itemName=models.CharField(max_length=50)
    
class ShopStock(models.Model):
    currentOwner=models.CharField(max_length=100)
    currentLocation=models.CharField(max_length=50)
    itemDesc=models.CharField(max_length=50)
    itemSN=models.CharField(max_length=200)
    date=models.CharField(max_length=50)

class ClearedShop(models.Model):
    shopName=models.CharField(max_length=50)
    itemSN=models.CharField(max_length=50)
    cleared=models.BooleanField(default=False)
    clearedDate=models.DateField(auto_now=True, auto_now_add=False)


