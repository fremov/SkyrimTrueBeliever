from django.shortcuts import render

from SkyrimTrueBeliever.settings import BASE_DIR
from stb_database_app.models import Races, InnateAbilities, Stones, Aedra


# Create your views here.
def home(request):
    return render(request, 'stb_database_app/navigation.html')


def base(request):
    return render(request, 'stb_database_app/basa.html')


def races(request):
    races = Races.objects.all()
    innate_abilities = InnateAbilities.objects.all()
    stones = Stones.objects.all()
    return render(request, 'stb_database_app/races.html', {
        'races': races,
        'innate_abilities': innate_abilities,
        'stones': stones,

    })

def aedra(request):
    aedras = Aedra.objects.all()
    return render(request, 'stb_database_app/aedra.html', {'aedras': aedras})

def daedra(request):
    daedras = Aedra.objects.all()
    return render(request, 'stb_database_app/daedra.html', {'daedras': daedras})