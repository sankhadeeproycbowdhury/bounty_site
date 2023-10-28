from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):

    peoples = [
        {'name':'sankha' , 'age':19},
        {'name':'Arman' , 'age':18},
        {'name':'sidharth' , 'age':17},
        {'name':'Archit' , 'age':16},
        {'name':'sarim' , 'age':19},
        {'name':'NIdhaan' , 'age':20},

    ]
    return render(request , "home/index.html" , context={'peoples':peoples , 'page':'Home'})


def about(request):
       context = {'page':'About'}
       return render(request , "home/about.html",context )

def contact(request):
       context = {'page':'Contact'}
       return render(request , "home/contact.html" ,context)

def success_page(request):
    return HttpResponse("<h1>Hey this is a Success page</h1>")

