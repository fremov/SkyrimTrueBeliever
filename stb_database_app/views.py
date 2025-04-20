from django.shortcuts import render

from SkyrimTrueBeliever.settings import BASE_DIR
from stb_database_app.models import Races


# Create your views here.
def home(request):
    return render(request, 'stb_database_app/navigation.html')

def base(request):
    return render(request, 'stb_database_app/basa.html')

def races(request):
    races = Races.objects.all()
    return render(request, 'stb_database_app/races.html', {'races': races})