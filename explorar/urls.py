from django.urls import path 
from . import views

app_name = "explorar"

urlpatterns = [
    path("", views.explorar_home, name='home'),
    path("adicionar/", views.explorar_adicionar, name="adicionar"),
    path("remover/<int:id>", views.explorar_remover, name='remover'),
    path("editar/<int:id>", views.explorar_editar, name='editar')
    
]