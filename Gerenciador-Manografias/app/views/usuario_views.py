
import re
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.models import User


@login_required
def cadastrar_usuario(request):
    if request.method == 'POST':
        form_usuario = CustomUserCreationForm(request.POST)
        if form_usuario.is_valid():
            user = form_usuario.save(commit=False)
            user.is_superuser = form_usuario.cleaned_data['is_superuser']
            user.save()
            return redirect('listar_usuarios')
    else:
        form_usuario = CustomUserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {"form_usuario": form_usuario})


def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('listar_manografias')
        else:
            messages.error(
                request, 'As credenciais do usuario estão incorretas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})


@login_required
def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')


@login_required
def listar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/listar_usuarios.html', {'usuarios': usuarios})


@login_required
def editar_usuario(request, id):
    usuario = get_object_or_404(User, id=id)

    if request.method == 'POST':
        form_usuario = CustomUserChangeForm(request.POST, instance=usuario)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_usuarios')
    else:
        form_usuario = CustomUserChangeForm(instance=usuario)

    return render(request, 'usuarios/editar_usuario.html', {'form_usuario': form_usuario})


@login_required
def remover_usuario(request, id):
    usuario = get_object_or_404(User, id=id)

    if request.method == "POST":
        usuario.delete()
        return redirect('listar_usuarios')

    return render(request, 'usuarios/confirma_exclusao.html', {'usuario': usuario})