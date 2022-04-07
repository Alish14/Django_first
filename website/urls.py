
from django.urls import path,include
from website.views import *

urlpatterns = [
    path('',index),
    path('aboutme/',about_me),
    path('contactme/',contact)

]