from django.urls import path
from . import views
urlpatterns = [
    #shopsassets
    path('shopsinventory/',views.shopsInventory,name="shopsinventory"),
    path('shopassets/<str:shopname>',views.ShopAssets.as_view(),name="shopassets")
    #shopasset/<shopid>
    #receive
    #despatch
    
]
