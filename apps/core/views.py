from django.shortcuts import render
from .models import Disciplina

def index(request):
    # Pega todas as disciplinas cadastradas no banco
    disciplinas = Disciplina.objects.all()
    return render(request, 'core/index.html', {'disciplinas': disciplinas})