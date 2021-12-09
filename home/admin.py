from django.contrib import admin

# Register your models here.

from .models import Entrenado, Niveles, Usuario

admin.site.register(Niveles)
admin.site.register(Usuario)
admin.site.register(Entrenado)
