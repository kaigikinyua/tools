from django.shortcuts import render,redirect,get_list_or_404
from django.views import View
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
#local imports
from accounts.forms import LoginForm

def index(request):
    return render(request,"accounts\index.html")

def logout(request):
    response=None
    try:
        logout(request)
        response=render(request,"accounts\logout.html")
    except:
        response=render(request,"accounts\logout.html",{"error":"Error while loggin out"})
    return response

class Login(View):
    def get(self,request):
        return render(request,"accounts\login.html")
    def post(self,request):
        u=LoginForm(request.POST)
        response=None
        if(u.is_valid()):
            user=u.cleaned_data
            authenticated=authenticate(username=user["username"],password=user["password"])
            if(authenticated!=None):
                login(request,authenticated)
                response=redirect("userpage")
            else:
                response=render(request,"accounts\login.html",{"error":"Incorrect credentials"})
        else:
            response=render(request,"accounts\login.html",{"error":"Please fill in all the fields"})
        return response

class UserPage(View):
    #@login_required(login_url='login/')
    def get(self,request):
        if(Authentication.userIsLoggedIn(request)):
            return render(request,"accounts\page.html")
        else:
            return redirect("login")
            
    def post(self,request):
        if(Authentication.userIsLoggedIn(request)):
            return render(request,"accounts\page.html")
        else:
            return redirect("login")

class Authentication:
    @staticmethod
    def userIsLoggedIn(request):
        try:
            if(request.user.is_authenticated):
                return True
        except:
            return False