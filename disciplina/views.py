from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from disciplina.models import Disciplina

class DisciplinaDetail(generic.DetailView):
    model = Disciplina

class DisciplinaNova(generic.CreateView):
    model = Disciplina
    fields = '__all__'

class DisciplinaLista(generic.ListView):
    model = Disciplina
    queryset = Disciplina.objects.all()

class DisciplinaUpdate(generic.UpdateView):
    model = Disciplina
    fields = ['projeto', 'nomeProfessor', 'idProfessor',]
    template_name_suffix = '_update_form'

class DisciplinaDelete(generic.DeleteView):
    model = Disciplina
    success_url = reverse_lazy('disciplina-lista')