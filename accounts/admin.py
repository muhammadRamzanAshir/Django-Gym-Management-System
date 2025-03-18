from django.contrib import admin
from .models import AuthForms

@admin.register(AuthForms)
class AuthFormsAdmin(admin.ModelAdmin):
    list_display = ('pargraph_login', 'pargraph_singup', 'girisback', 'kayitback')
    search_fields = ('pargraph_login', 'pargraph_singup')  # Make the subheadings searchable
