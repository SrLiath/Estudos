from django.shortcuts import render, redirect
from .models import pessoa

# Create your views here.
def home(request):
    pessoas = pessoa.objects.all()
    return render(request, 'login.html', {'pessoas':pessoas})
def salvar(request):
    vnome = request.POST.get("nome")
    pessoa.objects.create(nome=vnome)
    pessoas = pessoa.objects.all()
    return render(request, "login.html",{"pessoas":pessoas})
def editar(request, id):
    Pessoa = pessoa.objects.get(id=id)
    return render(request, 'update.html', {'Pessoa':Pessoa})

def update(request, id):
    vnome = request.POST.get("nome")
    Pessoa = pessoa.objects.get(id=id)
    Pessoa.nome = vnome
    Pessoa.save()
    return redirect(home)

def delete(request, id):
    Pessoa = pessoa.objects.get(id=id)
    Pessoa.delete()
    return redirect(home)