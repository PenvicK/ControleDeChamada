from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from aluno.models import Aluno

class AlunoDetail(generic.DetailView):
    model = Aluno

class AlunoNovo(generic.CreateView):
    model = Aluno
    fields = '__all__'

class AlunoLista(generic.ListView):
    model = Aluno
    queryset = Aluno.objects.all()

class AlunoUpdate(generic.UpdateView):
    model = Aluno
    fields = ['nome','usuarioDiscord', 'rfID',]
    template_name_suffix = '_update_form'

class AlunoDelete(generic.DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno-lista')