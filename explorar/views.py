from django.shortcuts import render, redirect, get_object_or_404
from .forms import ExplorarForm
from .models import ExplorarModel
from django.http import HttpRequest

# Create your views here.

def explorar_home(request):
    contexto = {
        "nome":"Sarahh",
        "adicionados":ExplorarModel.objects.all()
    }
    return render(request, 'explorar/home.html', contexto)

def explorar_adicionar(request:HttpRequest):
    if request.method =="POST":
        formulario = ExplorarForm(request.POST, request.FILES)
        if formulario.is_valid():    
            formulario.save()
            return redirect("explorar:home")

    contexto = {
        "form":ExplorarForm()
    }
    return render(request, 'explorar/adicionar.html', contexto)

def explorar_remover(request:HttpRequest, id):
    explorar = get_object_or_404(ExplorarModel, id=id)
    explorar.delete()
    return redirect("explorar:home")
    
def explorar_editar(request:HttpRequest, id):
    explorar = get_object_or_404(ExplorarModel, id=id)
    if request.method == "POST":
        formulario = ExplorarForm(request.POST,request.FILES, instance=explorar)
        if formulario.is_valid():
            formulario.save()
            return redirect("explorar:home")

    formulario = ExplorarForm(instance=explorar)
    context = {
        'form':formulario
    }
    return render(request, 'explorar/editar.html', context)
