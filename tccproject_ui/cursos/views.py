from django.shortcuts import render

from cursos.models import Curso


def home(request):
    cursos = Curso.objects.all()    
    return render(request, 'home.html', {'cursos': cursos})
