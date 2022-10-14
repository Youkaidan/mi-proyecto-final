from django.shortcuts import render
from ejemplo.models import Familiar

def index(request):
    return render(request, "ejemplo/saludar.html", {"nombre":"Erwin"})

def index_tres(request):
    return render(request, "ejemplo/saludar.html",
    {
        "notas":[1,2,3,4,5,6,7,8]
    })

def imc(request, peso, altura):
    imc = int(peso)/(int(altura)*int(altura)) #calcular el imc
    return render(request, "ejemplo/imc.html", {"imc":imc})

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "ejemplo/familiares.html", 
                                {"lista_familiares": lista_familiares})    