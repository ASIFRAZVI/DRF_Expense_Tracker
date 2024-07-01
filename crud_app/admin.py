from django.contrib import admin

# Register your models here.
from .models import create_expense

#register the model
admin.site.register(create_expense)
