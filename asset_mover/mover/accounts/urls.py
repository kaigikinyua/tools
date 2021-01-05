from django.urls import path 
from . import views
urlpatterns=[
  path('',views.index,name="index"),
  path('login',views.Login.as_view(),name="login"),
  path('userpage',views.UserPage.as_view(),name="userpage")  
]