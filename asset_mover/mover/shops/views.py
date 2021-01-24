from django.shortcuts import render
from django.views import View

# Create your views here.
def shopsInventory(request):
    return render(request,"shops/shopsinventory.html")

class ShopAssets(View):
    items=[
        {"desc":"Datecs FP 300","sn":"AD30102011","location":"MIS"},
        {"desc":"Hp Monitor","sn":"FBCAMCA920","location":"Shop"},
        {"desc":"Epson LX-300","sn":"*Q4293506","location":"Arseco"}
    ]
    def get(self,request,shopname):
        shopname=shopname
        return render(request,"shops/shopassets.html",{"shopname":shopname,"items":self.items})
    #login required
    def post(self,request,shopname):
        shopname=shopname
        return render(request,"shops/shopassets.html",{"shopname":shopname,"items":self.items})
