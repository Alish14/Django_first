import django


from django.shortcuts import render
from django.http import HttpResponse
def index_view(request):
    return HttpResponse("<h1>home page</h1>")
def about_me(request):
    return HttpResponse("<h1>about me page</h1>")

def contact(request):
    return HttpResponse("<h1>contact page</h1>")
    

