import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario 
from .forms import UsuarioForm
import requests
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login


def home(request):
    return render(request, 'app/home.html')


# Create your views here.



def register_view(request):
    form = UsuarioForm()
    
    return render(request, 'app/home.html', {'form': form}) 


def detail_view(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if usuario:
        return render(request, 'app/detail.html', {'usuario': usuario})


def delete_view(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if usuario:
        usuario.delete()    

def update_view(request, pk):
    usuario = Usuario.objects.get(pk=pk)
    if request.method == 'GET':
        form = UsuarioForm(instance=usuario)
        return render(request, 'app/update.html', {'usuario': usuario, 'form': form})
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.password = make_password(usuario.password)
            usuario.save()
            return redirect('')


def usuario_list(request):
    usuarios = Usuario.objects.all().order_by('id')
    return render(request, 'app/usuario_list.html', {'usuarios': usuarios})


def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'app/usuario_detail.html', {'usuario': usuario})


def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario_list')
    else:
        form = UsuarioForm()

    return render(request, 'app/usuario_form.html', {'form': form, 'titulo': 'Novo usuário'})


def usuario_update(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)

    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario_detail', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)

    return render(request, 'app/usuario_form.html', {'form': form, 'titulo': 'Editar usuário'})


def usuario_delete(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    usuario.delete()
    return redirect('usuario_list')