from django.contrib import admin
from webapp.models import signin
class Signin(admin.ModelAdmin):
    list_display=('Username','Password','FaviouriteCity')

admin.site.register(signin,Signin)    
# Register your models here.
