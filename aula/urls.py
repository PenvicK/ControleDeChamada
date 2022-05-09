from django.urls import path

from aula import views
from aula.views import AulaDetail, aula_list, AulaDelete

urlpatterns = [
    path('nova/', views.aula_form, name="aula_nova"),
    path('<int:pk>/', AulaDetail.as_view(), name='aula-detail'),
    path('lista/', views.aula_list, name='aula-lista'),
    # path('aula/<int:pk>/update/', AulaUpdate.as_view(), name='aula-update'),
    path('<int:pk>/delete/', AulaDelete.as_view(), name='aula-delete'),
]