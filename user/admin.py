from django.contrib import admin
from .models import*

# Register your models here.
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","message")

admin.site.register(tblcontact)
