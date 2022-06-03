from django.urls import path
from accounts.views import *


app_name='accounts'
urlpatterns = [
    path('login/',view_login,name='login'),
    path('logout/',view_logout,name='logout'),
    path('signup/',view_signup,name='signup'),
    





]
