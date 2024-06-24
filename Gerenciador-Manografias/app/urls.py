#from unicodedata import name
from django.contrib import admin
from django.urls import path
from .views.manografia_views import *
from .views.usuario_views import *
from .views.docente_views import *
from .views.discente_views import *
from .views.api_manografia import *
from .views.auditoria_views import*
from .views.chatbot import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title='API Eva',
        default_version='v1',
        description='API e documentação desenvolvidos para o trabalho de Sistemas Distribuídos, ministrada pelo Professor Alessandro Vivas',
        contact=openapi.Contact(email='evafrancisca@ufvjm.edu.br'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [

    path('', listar_manografias, name = 'listar_manografias'),
    path('remover_manografia/<int:id>', remover_manografia, name='remover_manografia'),
    path('pesquisar_manografias/', pesquisar_manografias, name='pesquisar_manografias'),
    path('listar_docentes', listar_docentes, name='listar_docentes'),
    path('cadastrar_manografia/', cadastrar_manografia, name = 'cadastrar_manografia'),
    path('editar_manografia/<int:id>', editar_manografia, name= 'editar_manografia'),
    path('cadastrar_docente/', cadastrar_docente, name='cadastrar_docente'),
    path('editar_docente/<int:id>', editar_docente, name='editar_docente'),
    path('remover_docente/<int:id>', remover_docente, name='remover_docente'),
    path('listar_discentes', listar_discentes, name='listar_discentes'),
    path('cadastrar_discentes/', cadastrar_discente, name='cadastrar_discente'),
    path('editar_discente/<int:id>', editar_discente, name='editar_discente'),
    path('remover_discente/<int:id>', remover_discente, name='remover_discente'),
        path('manografia_get', manografia_get, name='manografia_get'),
    path('manografia_get_id/<int:pk>',
        manografia_get_id, name='manografia_get_id'),
    path('manografia_post', manografia_post, name='manografia_post'),
    path('manografia_put/<int:pk>', manografia_put, name='manografia_put'),
    path('manografia_delete/<int:pk>',
        manografia_delete, name='manografia_delete'),
    path('swagger/', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-redoc'),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('editar_usuario/<int:id>', editar_usuario, name='editar_usuario'),
    path('remover_usuario/<int:id>', remover_usuario, name='remover_usuario'),
    path('listar_auditoria/', listar_auditoria, name='listar_auditoria'),
    path('chatbot', chatbot, name='chatbot')
    ]

