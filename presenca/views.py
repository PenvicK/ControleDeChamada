from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from presenca.models import Presenca




class PresencaDetail(generic.DetailView):
    model = Presenca

# class PresencaNova(generic.CreateView):
#     model = Presenca
#     fields = '__all__'

# class PresencaLista(generic.ListView):
#     model = Presenca
#     queryset = Presenca.objects.all()

class PresencaDelete(generic.DeleteView):
    model = Presenca
    success_url = reverse_lazy('presenca-lista')