from django.contrib import admin

# Register your models here.
from .models import Autor, Editorial, Libro

admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
