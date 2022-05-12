from django.urls import path

from presenca import views
from presenca.views import PresencaDetail, PresencaDelete

urlpatterns = [
    path('nova/', views.presenca_form, name="presenca_nova"),
    path('<int:pk>/', PresencaDetail.as_view(), name='presenca-detail'),
    path('lista/', views.presenca_list, name='presenca-lista'),
    # path('aula/<int:pk>/update/', AulaUpdate.as_view(), name='aula-update'),
    path('<int:pk>/delete/', PresencaDelete.as_view(), name='presenca-delete'),
]