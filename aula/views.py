from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from aula.models import Aula


class AulaNova(generic.CreateView):
    model = Aula
    fields = '__all__'

class AulaDetail(generic.DetailView):
    model = Aula

class AulaLista(generic.ListView):
    model = Aula
    queryset = Aula.objects.all()

class AulaUpdate(generic.UpdateView):
    model = Aula
    fields = ['dataHora',]
    template_name_suffix = '_update_form'

class AulaDelete(generic.DeleteView):
    model = Aula
    success_url = reverse_lazy('aula-lista')