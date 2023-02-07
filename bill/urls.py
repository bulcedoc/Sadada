
from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('pos_login/', pos_login , name="pos_login"),
    path('', pos_billing , name="pos_billing"),
    path('add_cart/', add_cart , name="add_cart"),
    path('check/', check, name="check")
    

]

