from django.contrib import admin
from .models import Plant, Care, Category
# Register your models here.

admin.site.register(Plant)
admin.site.register(Care)
admin.site.register(Category)