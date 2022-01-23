from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# view function basically do is take a requset from client side and respond to it (Request Handler)

# some other framworks call it as actions

def calculate():
      x = 1
      y = 2
      return x
    
def say_Hello( request ):

    # pull data from DB
    # transform
    # send Email

    x = calculate()

    return render(request, 'hello.html',  { 'name' : 'Mosh' })