from django.contrib import admin

from .models import Departamento, Inquilino, Contrato

admin.site.register(Departamento)
admin.site.register(Inquilino)
admin.site.register(Contrato)

