
from django.urls import path,include
from website.views import *

urlpatterns = [
    path('',index_view),
    path('aboutme/',about_me),
    path('contact me/',contact)

]