from django.urls import path

from disciplina import views
from disciplina.views import DisciplinaDelete, DisciplinaDetail

urlpatterns = [
    path('nova/', views.disciplina_form, name="disciplina_nova"),
    path('<int:pk>/', DisciplinaDetail.as_view(), name='disciplina-detail'),
    path('lista/', views.disciplina_list, name='disciplina-lista'),
    # path('aula/<int:pk>/update/', AulaUpdate.as_view(), name='aula-update'),
    path('<int:pk>/delete/', DisciplinaDelete.as_view(), name='disciplina-delete'),
]