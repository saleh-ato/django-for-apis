from django.contrib import admin
from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display=("id","title","body")

admin.site.register(Todo,TodoAdmin)