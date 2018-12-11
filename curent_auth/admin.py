from django.contrib import admin
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class PastsAdmin(admin.ModelAdmin):
    fields = ['username']
    list_display = ('username',)