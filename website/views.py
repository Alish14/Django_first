


from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')

def about_me(request):
    return HttpResponse("<h1>about me page</h1>")

def contact(request):
    return HttpResponse("<h1>contact page</h1>")
    

