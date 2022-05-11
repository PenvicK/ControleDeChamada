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
from django.urls import path, include

from index import views
from presenca.views import PresencaNova, PresencaDetail, PresencaLista, PresencaDelete

urlpatterns = [
    path('aula/', include('aula.urls')),
    path('aluno/', include('aluno.urls')),
    path('disciplina/', include('disciplina.urls')),
    path('index/', views.index,name='index'),

    path('presenca/nova/', PresencaNova.as_view(), name='presenca-nova'),
    path('presenca/<int:pk>/', PresencaDetail.as_view(), name='presenca-detail'),
    path('presenca/lista/', PresencaLista.as_view(), name='presenca-lista'),
    path('presenca/<int:pk>/delete/', PresencaDelete.as_view(), name='presenca-delete'),
]
