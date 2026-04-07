from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Painel Administrativo
    path('admin/', admin.site.urls),

    # Autenticação JWT (Sprint 2)
    # Rota para Login: envia email/senha e recebe o Token
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Rota para atualizar o Token sem precisar deslogar
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Rotas dos Módulos (Apps)
    path('api/usuarios/', include('apps.people.urls')),    # Gestão de Usuários 
    path('api/cursos/', include('apps.courses.urls')),      # CRUD de Cursos (Sprint 3) [cite: 85]
    path('api/salas/', include('apps.rooms.urls')),        # CRUD de Salas (Sprint 4) [cite: 110]
    path('api/grade/', include('apps.schedule.urls')),     # Grade Horária (Sprint 5) [cite: 135]
    path('api/core/', include('apps.core.urls')),          # Funcionalidades Base
]