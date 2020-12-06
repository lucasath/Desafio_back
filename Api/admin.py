from django.contrib import admin
from Api.models import *

# Register your models here.
class SolicitacoesAdmin(admin.ModelAdmin):
    
    list_display = ('data',)


admin.site.register(Solicitacao, SolicitacoesAdmin)
