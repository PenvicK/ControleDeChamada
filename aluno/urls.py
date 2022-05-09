from django.urls import path

from aluno import admin, views
from aluno.views import AlunoDetail, AlunoDelete

urlpatterns = [
    path('novo/', views.aluno_form, name='aluno-novo'),
    path('<int:pk>/', AlunoDetail.as_view(), name='aluno-detail'),
    path('lista/', views.aluno_list, name='aluno-lista'),
    # path('aluno/<int:pk>/update/', AlunoUpdate.as_view(), name='aluno-update'),
    path('<int:pk>/delete/', AlunoDelete.as_view(), name='aluno-delete'),

]