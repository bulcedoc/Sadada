from django.contrib import admin

from .models import *

admin.site.register(Users)
admin.site.register(Category)
admin.site.register(Products)
admin.site.register(Bill)
admin.site.register(Cart)