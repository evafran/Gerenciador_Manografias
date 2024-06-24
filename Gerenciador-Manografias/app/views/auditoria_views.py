from django.shortcuts import render
from ..models import ManografiaAudit
from django.contrib.auth.decorators import login_required


@login_required
def listar_auditoria(request):
    auditorias = ManografiaAudit.objects.all().order_by('-data_hora')
    return render(request, 'auditoria/listar_auditoria.html', {'auditorias': auditorias})