from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class ManografiaForm(forms.ModelForm):

    nota_final = forms.IntegerField(validators=[
        MinValueValidator(
            0, message='A nota final deve ser maior ou igual a 0.'),
        MaxValueValidator(
            100, message='A nota final deve ser menor ou igual a 100.')
    ])
    class Meta:
        model = Manografia_models
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'resumo': forms.Textarea(attrs={'class': 'form-control'}),
            'palavras_chave': forms.Textarea(attrs={'class': 'form-control'}),
            'data_entrega': forms.DateInput(attrs={'class': 'form-control'}),
            'banca_examinadora': forms.Textarea(attrs={'class': 'form-control'}),
            'nota_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'area_concentracao': forms.TextInput(attrs={'class': 'form-control'})
        }

class ManografiaPdfForm(forms.ModelForm):
    pdf = forms.FileField(required=False)
    
    class Meta:
        model = ArquivoPdf
        fields = ['pdf']

class DiscenteForm(forms.ModelForm):
    matricula = forms.CharField(validators=[
        MinLengthValidator(
            11, message='A matrícula deve ter exatamente 11 dígitos.'),
        MaxLengthValidator(
            11, message='A matrícula deve ter exatamente 11 dígitos.')
    ])
    class Meta:
        model = Discente
        fields = '__all__'

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    IS_SUPERUSER_CHOICES = [
        (True, 'Administrador'),
        (False, 'Professor/Aluno')
    ]
    is_superuser = forms.ChoiceField(
        choices=IS_SUPERUSER_CHOICES, widget=forms.RadioSelect, initial=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                'is_superuser', 'first_name', 'last_name', 'email')


class CustomUserChangeForm(UserChangeForm):
    IS_SUPERUSER_CHOICES = [
        (True, 'Administrador'),
        (False, 'Professor/Aluno')
    ]
    is_superuser = forms.ChoiceField(
        choices=IS_SUPERUSER_CHOICES, widget=forms.RadioSelect, initial=False)

    class Meta:
        model = User
        fields = ('username', 'is_superuser',
                'first_name', 'last_name', 'email')
