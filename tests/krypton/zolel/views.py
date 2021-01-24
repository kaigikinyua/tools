from django.shortcuts import render
from random import randrange
# Create your views here.
def index(request):
    templates=['d2.html','d.html']
    html=templates[randrange(0,2)]
    template="dynamic/{t}".format(t=html)
    return render(request,template)