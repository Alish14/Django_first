from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm,AccountAuthenticationForm



def view_login(request):
    if  not request.user.is_authenticated:
        form= AccountAuthenticationForm ()
        
        if request.method =='POST':
            form= AccountAuthenticationForm (request.POST)
            if form.is_valid():
                username=form.cleaned_data.get('username')
                password=form.cleaned_data.get('password')
                if not authenticate(email=username, password=password):
                        messages.add_message(request,messages.ERROR,"invalid login")
                account=authenticate(username=username,password=password)
                if account is not None:
                        login(request, account)
        return render(request,'accounts/login-username.html',{'form':form})


    else:
        return redirect('/')
@login_required
def view_logout(request):
        logout(request)
        return redirect('/')


def view_signup(request):
    user=request.user
    form =RegistrationForm()

    if   request.user.is_authenticated:
        return HttpResponse("you are already authenticated as %s"%user.email)
    if not request.user.is_authenticated:
        if request.POST:
            form = RegistrationForm(request.POST)

            if form.is_valid():
                print(form)
                form.save()
                return redirect('accounts:login')
    return render(request,'accounts/signup.html',{'form':form})



# Create your views here.
