from ..models import Discente


def cadastrar_discente(discente):
    Discente.objects.create(
        nome=discente.nome, sobrenome=discente.sobrenome, matricula=discente.matricula)


def listar_discentes(request):
    return Discente.objects.all().order_by('nome')


def listar_discente_id(id):
    return Discente.objects.get(id=id)


def editar_discente(discente_bd, novo_discente):
    discente_bd.nome = novo_discente.nome
    discente_bd.sobrenome = novo_discente.sobrenome
    discente_bd.matricula = novo_discente.matricula
    discente_bd.save(force_update=True)


def excluir_discente(discente_bd):
    discente_bd.delete()