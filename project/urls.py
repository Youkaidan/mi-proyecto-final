"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from ejemplo.views import (index, index_tres, imc, monstrar_familiares
                            ,BuscarFamiliar, AltaFamiliar, FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar)
from blog.views import index as blog_index                           
from blog.views import InsertJuego, InsertDesarrollador, InsertNoticias, BuscarJuego

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar/', index), # ESTA ES LA NUEVA FUNCTION
    path('mostrar-notas/', index_tres), 
    path('imc/<peso>/<altura>/', imc), 
    path('mi-familia/', monstrar_familiares), 
    path('mi-familia/buscar', BuscarFamiliar.as_view()), # clase 20 form
    path('mi-familia/alta', AltaFamiliar.as_view()), # clase 21
    path('panel-familia/', FamiliarList.as_view(), name="familiar-list"), #clase 22
    path('panel-familia/crear', FamiliarCrear.as_view(), name="familiar-crear"), #clase 22
    path('panel-familia/<int:pk>/borrar', FamiliarBorrar.as_view(), name="familiar-borrar"), #clase 22
    path('panel-familia/<int:pk>/actualizar', FamiliarActualizar.as_view(), name="familiar-actualizar"),

    #BLOG - PROYECTO FINAL
    path('blog/', include('blog.urls')),
    
]

#if not settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)