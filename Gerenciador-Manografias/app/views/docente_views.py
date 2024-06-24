from django.shortcuts import render, redirect
from ..forms import DocenteForm
from ..entidades.docente import Docente
from ..services import docente_service


def cadastrar_docente(request):
    if request.method == 'POST':
        form_docente = DocenteForm(request.POST)
        if form_docente.is_valid():
            nome = form_docente.cleaned_data['nome']
            sobrenome = form_docente.cleaned_data['sobrenome']

            novo_docente = Docente(nome=nome, sobrenome=sobrenome)
            docente_service.cadastrar_docente(novo_docente)
            return redirect('listar_docentes')
    else:
        form_docente = DocenteForm()
    return render(request, 'docente/form_docente.html', {'form_docente': form_docente})


def listar_docentes(request):
    docentes = docente_service.listar_docentes(request.user)
    return render(request, 'docente/listar_docentes.html', {'docentes': docentes})


def editar_docente(request, id):
    docente_bd = docente_service.listar_docente_id(id)
    form_docente = DocenteForm(request.POST or None, instance=docente_bd)
    if form_docente.is_valid():
        nome = form_docente.cleaned_data['nome']
        sobrenome = form_docente.cleaned_data['sobrenome']

        novo_docente = Docente(nome=nome, sobrenome=sobrenome)
        docente_service.editar_docente(docente_bd, novo_docente)
        return redirect('listar_docentes')

    return render(request, 'docente/form_docente.html', {'form_docente': form_docente})


def remover_docente(request, id):
    docente_bd = docente_service.listar_docente_id(id)
    if request.method == 'POST':
        docente_service.excluir_docente(docente_bd)
        return redirect('listar_docentes')
    return render(request, 'docente/confirmar_exclusao_docente.html', {'docente': docente_bd})