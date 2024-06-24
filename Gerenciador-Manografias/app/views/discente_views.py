from django.shortcuts import render, redirect
from ..forms import DiscenteForm
from ..entidades.discente import Discente
from ..services import discente_service


def cadastrar_discente(request):
    if request.method == 'POST':
        form_discente = DiscenteForm(request.POST)
        if form_discente.is_valid():
            nome = form_discente.cleaned_data['nome']
            sobrenome = form_discente.cleaned_data['sobrenome']
            matricula = form_discente.cleaned_data['matricula']

            novo_discente = Discente(
                nome=nome, sobrenome=sobrenome, matricula=matricula)
            discente_service.cadastrar_discente(novo_discente)
            return redirect('listar_discentes')
    else:
        form_discente = DiscenteForm()
    return render(request, 'discente/form_discente.html', {'form_discente': form_discente})


def listar_discentes(request):
    discentes = discente_service.listar_discentes(request.user)
    return render(request, 'discente/listar_discentes.html', {'discentes': discentes})


def editar_discente(request, id):
    discente_bd = discente_service.listar_discente_id(id)
    form_discente = DiscenteForm(request.POST or None, instance=discente_bd)
    if form_discente.is_valid():
        nome = form_discente.cleaned_data['nome']
        sobrenome = form_discente.cleaned_data['sobrenome']
        matricula = form_discente.cleaned_data['matricula']

        novo_discente = Discente(
            nome=nome, sobrenome=sobrenome, matricula=matricula)
        discente_service.editar_discente(discente_bd, novo_discente)
        return redirect('listar_discentes')

    return render(request, 'discente/form_discente.html', {'form_discente': form_discente})


def remover_discente(request, id):
    discente_bd = discente_service.listar_discente_id(id)
    if request.method == 'POST':
        discente_service.excluir_discente(discente_bd)
        return redirect('listar_discentes')
    return render(request, 'discente/confirmar_exclusao_discente.html', {'discente': discente_bd})