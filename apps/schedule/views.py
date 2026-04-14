from django.shortcuts import render
from apps.schedule.models import Aula
from apps.rooms.models import Sala
from django.contrib.auth import get_user_model

User = get_user_model()

def dashboard_grade(request):
    # Pegamos todos os dados para mandar para a tela
    aulas = Aula.objects.all()
    salas = Sala.objects.filter(ativo=True)
    professores = User.objects.filter(is_staff=True)
    
    contexto = {
        'aulas': aulas,
        'salas': salas,
        'professores': professores,
    }
    return render(request, 'schedule/dashboard.html', contexto)