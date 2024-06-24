from ..models import Manografia_models, ArquivoPdf


def cadastrar_manografia(manografia):
    Manografia_models.objects.create(
        titulo=manografia.titulo,
        autor=manografia.autor,
        orientador=manografia.orientador,
        coorientador=manografia.coorientador,
        resumo=manografia.resumo,
        palavras_chave=manografia.palavras_chave,
        data_entrega=manografia.data_entrega,
        banca_examinadora=manografia.banca_examinadora,
        nota_final=manografia.nota_final,
        area_concentracao=manografia.area_concentracao
    )


def listar_manografias():
    return Manografia_models.objects.all().order_by('titulo')


def listar_manografia_id(id):
    return Manografia_models.objects.get(id=id)


def editar_manografia(manografia_bd, nova_manografia):
    manografia_bd.titulo = nova_manografia.titulo
    manografia_bd.autor = nova_manografia.autor
    manografia_bd.orientador = nova_manografia.orientador
    manografia_bd.coorientador = nova_manografia.coorientador
    manografia_bd.resumo = nova_manografia.resumo
    manografia_bd.palavras_chave = nova_manografia.palavras_chave
    manografia_bd.data_entrega = nova_manografia.data_entrega
    manografia_bd.banca_examinadora = nova_manografia.banca_examinadora
    manografia_bd.nota_final = nova_manografia.nota_final
    manografia_bd.save()


def remover_manografia(manografia_bd):
    manografia_bd.delete()


def buscar_pdf():
    return ArquivoPdf.objects.all()


def buscar_pdf_id(id):
    try:
        return ArquivoPdf.objects.get(manografia_id=id)
    except ArquivoPdf.DoesNotExist:
        return None


def remover_pdf(pdf_bd):
    pdf_bd.delete()