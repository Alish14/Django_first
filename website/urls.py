
from django.urls import path,include
from website.views import *

urlpatterns = [
    path('home/',index),
    path('aboutme/',about_me),
    path('contact me/',contact)

]