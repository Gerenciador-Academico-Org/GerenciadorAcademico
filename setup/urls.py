from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls), # CORREÇÃO AQUI
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/usuarios/', include('apps.people.urls')),
    path('api/cursos/', include('apps.courses.urls')),
    path('api/salas/', include('apps.rooms.urls')),
    path('api/grade/', include('apps.schedule.urls')),
]