


from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')

def about_me(request):
    return render(request,'about_me.html')

def contact(request):
    return render(request,'contact.html')
    

