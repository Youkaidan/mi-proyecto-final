from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View 
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from blog.models import Configuracion, Juego, Desarrollador, Noticias
from blog.forms import BuscarJ ,JuegoForm, DesarrolladorForm, NoticiasForm


#@login_required
def index(request):
    configuracion = Configuracion.objects.first()
    ultimo_juego = Juego.objects.last()
    ultima_noticia = Noticias.objects.last()
    noticias = Noticias.objects.order_by('-fecha').all()
    return render(request, 'blog/index.html', {'configuracion': configuracion
                                                ,'ultimo_juego': ultimo_juego
                                                ,'ultima_noticia': ultima_noticia
                                                ,'Noticias': noticias})

def about(request):
    configuracion = Configuracion.objects.first()
    ultimo_juego = Juego.objects.last()
    return render(request, 'blog/about.html', {'configuracion': configuracion
                                                ,'ultimo_juego': ultimo_juego} )                                                

class InsertJuego(LoginRequiredMixin, View):

    form_class = JuegoForm
    template_name = 'blog/juego_insert.html'
    initial = {"nombre_juego":"", "desarrollador":"", "genero":"", "cantidad_jugadores":"", "resena":""}

    def get(self, request):
        configuracion = Configuracion.objects.first()
        ultimo_juego = Juego.objects.last()

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form
                                                    ,'configuracion': configuracion
                                                    ,'ultimo_juego': ultimo_juego})

    def post(self, request):
        configuracion = Configuracion.objects.first()
        ultimo_juego = Juego.objects.last()

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se ingres?? con ??xito el Juego: {form.cleaned_data.get('nombre_juego')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form 
                                                        ,'msg_exito': msg_exito
                                                        ,'configuracion': configuracion
                                                        ,'ultimo_juego': ultimo_juego})
        
        return render(request, self.template_name, {"form": form})

class InsertDesarrollador(LoginRequiredMixin, View):

    form_class = DesarrolladorForm
    template_name = 'blog/desarrollador_insert.html'
    initial = {"nombre_desarrollador":"", "pais":"", "anno_fundacion":""}

    def get(self, request):
        configuracion = Configuracion.objects.first()
        ultimo_juego = Juego.objects.last()

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form
                                                    ,'configuracion': configuracion
                                                    ,'ultimo_juego': ultimo_juego})

    def post(self, request):
        configuracion = Configuracion.objects.first()
        ultimo_juego = Juego.objects.last()

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se ingres?? con ??xito el Desarrollador: {form.cleaned_data.get('nombre_desarrollador')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form 
                                                        ,'msg_exito': msg_exito
                                                        ,'configuracion': configuracion
                                                        ,'ultimo_juego': ultimo_juego})
        
        return render(request, self.template_name, {"form": form})

class InsertNoticias(LoginRequiredMixin, View):
    
    form_class = NoticiasForm
    template_name = 'blog/noticias_insert.html'
    initial = {"titulo":"", "sub_titulo":"", "contenido":""}

    def get(self, request):
        configuracion = Configuracion.objects.first()
        ultimo_juego = Juego.objects.last()

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form
                                                    ,'configuracion': configuracion
                                                    ,'ultimo_juego': ultimo_juego})

    def post(self, request):
        configuracion = Configuracion.objects.first()
        ultimo_juego = Juego.objects.last()

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"Se ingres?? con ??xito la Noticia: {form.cleaned_data.get('titulo')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form 
                                                        ,'msg_exito': msg_exito
                                                        ,'configuracion': configuracion
                                                        ,'ultimo_juego': ultimo_juego})
        
        return render(request, self.template_name, {"form": form})        


class BuscarJuego(View):

    form_class = BuscarJ
    template_name = 'blog/buscarj.html'
    initial = {"nombre_juego":""}

    def get(self, request):
        configuracion = Configuracion.objects.first()
        ultimo_juego = Juego.objects.last()       

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form
                                                    ,'configuracion': configuracion
                                                    ,'ultimo_juego': ultimo_juego})

    def post(self, request):
        configuracion = Configuracion.objects.first()
        ultimo_juego = Juego.objects.last()

        form = self.form_class(request.POST)
        if form.is_valid():
            nombre_juego = form.cleaned_data.get("nombre_juego")
            lista_juegos = Juego.objects.filter(nombre_juego__icontains=nombre_juego).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form
                                                        ,'lista_juegos':lista_juegos
                                                        ,'configuracion': configuracion
                                                        ,'ultimo_juego': ultimo_juego})

        return render(request, self.template_name, {"form": form})          

##V2 CON GENERIC VIEWS

##Contexto base para heredar en vistas
class CommonMixinExample(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['configuracion'] = Configuracion.objects.first()
        context['ultimo_juego'] = Juego.objects.last()
        return context

class ListNoticia(CommonMixinExample, ListView):
    model = Noticias    

class CreateNoticia(LoginRequiredMixin, CommonMixinExample, CreateView):
    model = Noticias
    fields = ['titulo', 'sub_titulo', 'contenido', 'imagen']
    success_url = reverse_lazy("list-noticia")

class DetailNoticia(CommonMixinExample, DetailView):
    model = Noticias

class UpdateNoticia(LoginRequiredMixin, CommonMixinExample, UpdateView):
    model = Noticias
    fields = ['titulo', 'sub_titulo', 'contenido', 'imagen']
    success_url = reverse_lazy("list-noticia")

class DeleteNoticia(LoginRequiredMixin, CommonMixinExample, DeleteView):
    model = Noticias
    success_url = reverse_lazy("list-noticia")

class SearchNoticiaByName(CommonMixinExample, ListView):
    def get_queryset(self):
        blog_titulo = self.request.GET.get('titulo')
        return Noticias.objects.filter(titulo__icontains=blog_titulo)     
 
class BlogLogin(CommonMixinExample, LoginView):
    template_name = 'blog/blog_login.html'
    next_page = reverse_lazy("index-blog")

class BlogLogout(CommonMixinExample, LogoutView):
    template_name = 'blog/blog_logout.html'     

class BlogSignUp(LoginRequiredMixin, CommonMixinExample, CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("blog-login")
    template_name = "registration/signup.html"

class ProfileUpdate(LoginRequiredMixin, CommonMixinExample, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy("index-blog")    
    template_name = 'blog/user_form.html'   
