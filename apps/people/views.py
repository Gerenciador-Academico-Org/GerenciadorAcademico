from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer

class IsCoordenadorGeral(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.papel == 'coordenador_geral')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action in ['list', 'create', 'update', 'partial_update', 'destroy']:
            return [IsCoordenadorGeral()]
        return [permissions.IsAuthenticated()]