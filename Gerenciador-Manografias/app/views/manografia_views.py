from ..models import Manografia_models
from django.shortcuts import redirect, render
from ..forms import ManografiaForm, ManografiaPdfForm
from ..models import ArquivoPdf, ManografiaAudit
from ..models import ArquivoPdf
from ..services import manografia_service
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def cadastrar_manografia(request):
    form_pdf = ManografiaPdfForm(request.POST)
    if request.method == "POST":
        form_manografia = ManografiaForm(request.POST)
        pdf = request.FILES.get('pdf')
        if pdf:
            if form_manografia.is_valid() and form_pdf.is_valid():
                manografia = form_manografia.save()
                ArquivoPdf.objects.create(manografia=manografia, pdf=pdf)

                return redirect('listar_manografias')
        else:
            messages.error(request, 'Por favor, insira um arquivo PDF.')
    else:
        form_manografia = ManografiaForm()

    return render(request, 'manografia/form_manografia.html', {"form_manografia": form_manografia, 'form_pdf': form_pdf})

@login_required
def editar_manografia(request, id):
    manografia_bd = manografia_service.listar_manografia_id(id)
    pdf_bd = manografia_service.buscar_pdf_id(id)
    if pdf_bd:
        form_pdf = ManografiaPdfForm(request.POST, instance=pdf_bd)
    else:
        form_pdf = ManografiaPdfForm()

    if request.method == 'POST':
        form_manografia = ManografiaForm(request.POST, instance=manografia_bd)
        pdf = request.FILES.get('pdf')

        if form_manografia.is_valid():
            manografia = form_manografia.save()
            ManografiaAudit.objects.create(
                titulo_manografia=manografia.titulo,
                manografia=manografia,
                usuario=request.user,
                acao='atualização',
                detalhes='Manografia atualizada com sucesso.'
            )
            if pdf:
                if pdf_bd:
                    manografia_service.remover_pdf(pdf_bd)
                ArquivoPdf.objects.create(manografia=manografia, pdf=pdf)

            return redirect('listar_manografias')
    else:
        form_manografia = ManografiaForm(instance=manografia_bd)

    return render(request, 'manografia/form_manografia.html', {'form_manografia': form_manografia, 'form_pdf': form_pdf})



def listar_manografias(request):
    manografias = manografia_service.listar_manografias()
    pdfs = manografia_service.buscar_pdf()

    return render(request, 'manografia/listar_manografias.html', {'manografias': manografias, 'pdfs': pdfs})


def remover_manografia(request, id):
    manografia_bd = manografia_service.listar_manografia_id(id)
    pdf_bd = manografia_service.buscar_pdf_id(id)
    if request.method == "POST":
        manografia_service.remover_manografia(manografia_bd)
        if pdf_bd is not None:
            manografia_service.remover_pdf(pdf_bd)

        return redirect('listar_manografias')

    return render(request, 'manografia/confirma_exclusao.html', {'manografia': manografia_bd})


def pesquisar_manografias(request):
    pdfs = manografia_service.buscar_pdf()
    if request.method == "GET":
        termo_pesquisa = request.GET.get('termo_pesquisa').strip()
        manografias = Manografia_models.objects.filter(
            Q(titulo__icontains=termo_pesquisa) |
            Q(autor__nome__icontains=termo_pesquisa) |
            Q(autor__sobrenome__icontains=termo_pesquisa) |
            Q(orientador__nome__icontains=termo_pesquisa) |
            Q(orientador__sobrenome__icontains=termo_pesquisa) |
            Q(coorientador__nome__icontains=termo_pesquisa) |
            Q(coorientador__sobrenome__icontains=termo_pesquisa)
        )

        return render(request, 'manografia/pesquisa_manografias.html', {'manografias': manografias, 'termo_pesquisa': termo_pesquisa, 'pdfs': pdfs})

    return render(request, 'manografia/pesquisa_manografias.html')