from django.shortcuts import render
from ejemplo.models import Familiar
from ejemplo.forms import Buscar ,FamiliarForm # <--- CLASE 20 FORM y 21
from django.views import View # <-- CLASE 20 FORM

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

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'ejemplo/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})

        return render(request, self.template_name, {"form": form})         

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'ejemplo/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})