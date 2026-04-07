from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, VinculoUsuarioCurso

# Personalizando a visualização do Usuário no Admin
class MyUserAdmin(UserAdmin):
    model = User
    # Adicionando nossos campos personalizados (papel e telefone) à interface
    fieldsets = UserAdmin.fieldsets + (
        ('Informações Acadêmicas', {'fields': ('papel', 'telefone', 'ativo')}),
    )
    list_display = ['email', 'first_name', 'papel', 'is_staff', 'ativo']

# Registrando os modelos
admin.site.register(User, MyUserAdmin)
admin.site.register(VinculoUsuarioCurso)