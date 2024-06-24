from atexit import register
from unicodedata import name
from django import template

register = template.Library()

@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name='display_role')
def display_role(value):
    if value:
        return 'Administrador'
    return 'Professor/Aluno'