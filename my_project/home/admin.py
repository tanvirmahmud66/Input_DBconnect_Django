from django.contrib import admin
from home.models import Reg

# Register your models here.
class HomeReg(admin.ModelAdmin):
    list_display = ('name', 'email', 'password', 'contact')

admin.site.register(Reg, HomeReg)
