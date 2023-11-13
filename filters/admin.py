from django.contrib import admin

# Register your models here.
from .models import Category, Criteria

admin.site.register(Category)
admin.site.register(Criteria)