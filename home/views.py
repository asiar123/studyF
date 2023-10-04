from django.shortcuts import render
from person.models import Persona
from user.models import Usuario
# Create your views here.

def index(request):
    persons = Persona.objects.all()
    users = Usuario.objects.all()
    context = {'persons':persons,'users':users}
    return render(request, 'home/index.html', context)