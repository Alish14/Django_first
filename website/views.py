


from django.http import HttpResponseRedirect
from django.shortcuts import render
from website.forms import ContactForm ,Newsletterform
from django.contrib import messages
def index(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.name="anonymous"
            post.save()
            messages.success(request,'your ticket submited successfuly')
    else:
        messages.add_message(request,messages.ERROR,"your ticket didn't submited")
    form=ContactForm()
    return render(request,'website/contact.html',{'form':form})
def newsletter_view(request):

    if request.method =='POST':
        form=Newsletterform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')



