from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User # Ajuste se o nome do seu modelo for diferente (ex: CustomUser)

class CustomUserAdmin(UserAdmin):
    model = User
    
    # Esta é a linha mágica que adiciona o E-mail na tela de "Adicionar Usuário" (o popup do botão +)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Pessoais Obrigatórias', {'fields': ('email',)}),
    )

# Registra o modelo com as novas regras visuais
admin.site.register(User, CustomUserAdmin)