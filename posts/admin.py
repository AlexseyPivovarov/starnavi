from django.contrib import admin
from .models import Posts


# Register your models here.
@admin.register(Posts)
class PastsAdmin(admin.ModelAdmin):
    fields = ['title', 'body', 'data', 'like', 'unlike', 'user']
    list_display = ('title', 'body', 'data', 'like', 'unlike', 'user')
