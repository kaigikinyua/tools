from django.db import models

class UserItem(models.Model):
    itemName=models.CharField(max_length=50)
    
class Owner(models.Model):
    currentOwner=models.CharField(max_length=100)
    itemDesc=models.CharField(max_length=50)
    itemSN=models.CharField(max_length=200)
    date=models.CharField(max_length=50)

class PC(models.Model):
    owner=models.CharField(max_length=50)
    pcModel=models.CharField(max_length=50)
    osVer=models.CharField(max_length=50)
    ram=models.IntegerField()
    cpu=models.CharField(max_length=50)
    activated=models.BooleanField(default=True)

class ClearedOwner(models.Model):
    owner=models.CharField(max_length=50)
    itemSN=models.CharField(max_length=50)
    cleared=models.BooleanField(default=False)
    clearedDate=models.DateField(auto_now=True, auto_now_add=True)
    location=models.CharField(max_length=50)


