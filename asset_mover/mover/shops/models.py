from django.db import models

# Create your models here.
class ShopItem(models.Model):
    itemName=models.CharField(max_length=50)
    def __str__(self):
        return self.itemName

class ShopStock(models.Model):
    currentOwner=models.CharField(max_length=100)
    currentLocation=models.CharField(max_length=50)
    itemFunc=models.CharField(default="",max_length=100)
    itemDesc=models.CharField(max_length=50)
    itemSN=models.CharField(max_length=200)
    date=models.CharField(max_length=50)
    def __str__(self):
        return "{own} {func} {loc} {desc}".format(own=self.currentOwner,func=self.itemFunc,loc=self.currentLocation,desc=self.itemDesc)

class SimCard(models.Model):
    sim_choices=[('data',"Data"),('mpesa',"Mpesa")]
    shopname=models.CharField(max_length=50)
    sim_use=models.CharField(default="Data",choices=sim_choices, max_length=50)
    sn=models.CharField(max_length=50)
    phone_num=models.CharField(default=0,max_length=50)
    #pin1
    #pin2
    puk1=models.CharField(max_length=50)
    puk2=models.CharField(max_length=50)
    #location
    def __str__(self):
        return "{name} {sn} {num}".format(name=self.shopname,sn=self.sn, num=self.phone_num)
#Data Sim top up

class ClearedShop(models.Model):
    shopName=models.CharField(max_length=50)
    itemSN=models.CharField(max_length=50)
    cleared=models.BooleanField(default=False)
    clearedDate=models.DateField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return "{own} {sn} {cl}".format(own=self.shopName,sn=self.itemSN,cl=self.cleared)


