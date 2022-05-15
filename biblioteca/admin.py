from django.contrib import admin
from .models import Biblioteca, Livro, Cliente, Requesicao


# Register your models here.
admin.site.register(Biblioteca)
admin.site.register(Livro)
admin.site.register(Cliente)
admin.site.register(Requesicao)