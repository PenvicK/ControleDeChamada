"""ControleDeChamada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from aluno.views import AlunoNovo, AlunoLista, AlunoUpdate, AlunoDelete, AlunoDetail
# from aula.views import AulaNova, AulaDetail, AulaLista, AulaUpdate, AulaDelete
from aula import views
from aula.views import AulaDetail, AulaDelete
from disciplina.views import DisciplinaNova, DisciplinaDetail, DisciplinaLista, DisciplinaUpdate, DisciplinaDelete
from presenca.views import PresencaNova, PresencaDetail, PresencaLista, PresencaDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aluno/novo/', AlunoNovo.as_view(), name='aluno-novo'),
    path('aluno/<int:pk>/', AlunoDetail.as_view(), name='aluno-detail'),
    path('aluno/lista/', AlunoLista.as_view(), name='aluno-lista'),
    path('aluno/<int:pk>/update/', AlunoUpdate.as_view(), name='aluno-update'),
    path('aluno/<int:pk>/delete/', AlunoDelete.as_view(), name='aluno-delete'),

    path('aula/nova/', views.aula_form, name='aula_nova'),
    path('aula/<int:pk>/', AulaDetail.as_view(), name='aula-detail'),
    path('aula/lista/', views.aula_list, name='aula-lista'),
    # path('aula/<int:pk>/update/', AulaUpdate.as_view(), name='aula-update'),
    path('aula/<int:pk>/delete/', AulaDelete.as_view(), name='aula-delete'),

    path('disciplina/nova/', DisciplinaNova.as_view(), name='disciplina-nova'),
    path('disciplina/<int:pk>/', DisciplinaDetail.as_view(), name='disciplina-detail'),
    path('disciplina/lista/', DisciplinaLista.as_view(), name='disciplina-lista'),
    path('disciplina/<int:pk>/update/', DisciplinaUpdate.as_view(), name='disciplina-update'),
    path('disciplina/<int:pk>/delete/', DisciplinaDelete.as_view(), name='disciplina-delete'),

    path('presenca/nova/', PresencaNova.as_view(), name='presenca-nova'),
    path('presenca/<int:pk>/', PresencaDetail.as_view(), name='presenca-detail'),
    path('presenca/lista/', PresencaLista.as_view(), name='presenca-lista'),
    path('presenca/<int:pk>/delete/', PresencaDelete.as_view(), name='presenca-delete'),
]
