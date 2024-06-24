from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from django.db import models

class Discente(models.Model):
    nome =models.CharField(max_length=100, null=False, blank=False)
    sobrenome=models.CharField(max_length=100, null=False, blank=False)
    matricula=models.BigIntegerField()

    def __str__(self):
        return f'{self.nome} {self.sobrenome} - ({self.matricula})'

class Docente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    sobrenome = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

class Manografia_models(models.Model):
    titulo = models.CharField(max_length=500)
    autor = models.ForeignKey(Discente, on_delete=models.CASCADE, null=False, blank=False)
    orientador = models.ForeignKey(Docente, related_name='manografias_orientadas', on_delete=models.CASCADE, null=False, blank=False)
    coorientador = models.ForeignKey(Docente, related_name='manografias_coorientadas', on_delete=models.CASCADE, null=False, blank=False)
    resumo = models.TextField(null=False, blank=False)
    palavras_chave = models.CharField(max_length=150, null=False, blank=False)
    data_entrega = models.DateField(null=False, blank=False)
    banca_examinadora = models.CharField(
        max_length=300, null=False, blank=False)
    nota_final = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], null=False, blank=False)
    area_concentracao = models.CharField(
        max_length=100, null=False, blank=False)


    def __str__(self):
        return self.titulo
    

class ManografiaAudit(models.Model):
    titulo_manografia = models.CharField(max_length=500, blank=True)
    manografia = models.ForeignKey(
        Manografia_models, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    acao = models.CharField(max_length=50)
    data_hora = models.DateTimeField(auto_now_add=True)
    detalhes = models.TextField()

    def __str__(self):
        return f"{self.titulo_manografia} - {self.acao} por {self.usuario.username}"



class ArquivoPdf(models.Model):
    pdf = models.FileField('pdf', upload_to='', null=False, blank= True)
    manografia = models.ForeignKey(
        Manografia_models,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ('pk',)
        verbose_name = 'pdf'
        verbose_name_plural = 'pdfs'

    def __str__(self):
        return str(self.manografia)