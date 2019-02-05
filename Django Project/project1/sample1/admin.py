from django.contrib import admin
from .models import Pet
@admin.register(Pet)
class adminPet(admin.ModelAdmin):
    pass