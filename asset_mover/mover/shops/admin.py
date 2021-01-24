from django.contrib import admin
from shops.models import *
# Register your models here.
admin.site.register(ShopItem)
admin.site.register(SimCard)
admin.site.register(ShopStock)
admin.site.register(ClearedShop)

