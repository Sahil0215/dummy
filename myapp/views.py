from django.shortcuts import render,redirect
from .models import *


def home(request):
    if request.method=="POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        item = Item (name=name, phone=phone)

        item.save()
        redirect('home')
    
    item=Item.objects.all()
    var = {
        "item" : item
    }
    return render(request, 'home.html' , var)
# Create your views here.
