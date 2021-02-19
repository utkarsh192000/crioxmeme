from django.contrib import admin
from .models import Meme
# Register your models here.
@admin.register(Meme)
class MemeAdmin(admin.ModelAdmin):
    list_display = ('id',"name","caption","url")