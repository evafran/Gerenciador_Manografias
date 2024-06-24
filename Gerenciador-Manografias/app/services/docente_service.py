from ..models import Docente


def cadastrar_docente(docente):
    Docente.objects.create(nome=docente.nome, sobrenome=docente.sobrenome)


def listar_docentes(request):
    return Docente.objects.all().order_by('nome')


def listar_docente_id(id):
    return Docente.objects.get(id=id)


def editar_docente(docente_bd, novo_docente):
    docente_bd.nome = novo_docente.nome
    docente_bd.sobrenome = novo_docente.sobrenome
    docente_bd.save(force_update=True)


def excluir_docente(docente_bd):
    docente_bd.delete()