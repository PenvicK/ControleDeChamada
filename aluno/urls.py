from django.urls import path

from aluno import admin, views
from aluno.views import AlunoDetail, AlunoDelete

urlpatterns = [
    path('aluno/novo/', views.aluno_form, name='aluno-novo'),
    path('aluno/<int:pk>', AlunoDetail.as_view(), name='aluno-detail'),
    path('aluno/lista/', views.aluno_list, name='aluno-lista'),
    # path('aluno/<int:pk>/update/', AlunoUpdate.as_view(), name='aluno-update'),
    path('aluno/<int:pk>/delete/', AlunoDelete.as_view(), name='aluno-delete'),
    path('discord/<str:nickName>/<str:id>', views.some_view, name='aluno-discord'),

    path('professor/novo/', views.professor_form, name='professor-novo'),
    path('professor/<int:pk>', AlunoDetail.as_view(), name='professor-detail'),
    path('professor/lista/', views.professor_list, name='professor-lista'),
    # path('aluno/<int:pk>/update/', AlunoUpdate.as_view(), name='aluno-update'),
    path('professor/<int:pk>/delete/', AlunoDelete.as_view(), name='professor-delete'),

]