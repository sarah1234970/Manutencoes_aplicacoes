from django.contrib import admin
from .models import ExplorarModel # Importa o modelo Membros da aplicação atual

# Define uma classe de configuração personalizada para o modelo Membros no admin.
class explorarAdmin(admin.ModelAdmin):

    # Define quais campos serão exibidos na lista de membros no painel de administração.
    list_display = ('titulo','descricao','categoria','completo','imagem')

# Registra o modelo Membros no site de administração do Django,
# usando a configuração personalizada MembrosAdmin.
admin.site.register(ExplorarModel, explorarAdmin)
# Register your models here.
