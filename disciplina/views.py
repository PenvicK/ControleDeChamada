from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from aluno.models import Aluno
from disciplina.forms import FormDisciplinaNova
from disciplina.models import Disciplina

def disciplina_form(request):
    if request.method == "GET":
        form = FormDisciplinaNova()
        context = {
            'form': form
        }
        return render(request, 'disciplina/disciplina_form.html', context=context)
    else:
        form = FormDisciplinaNova(request.POST)
        if form.is_valid():
            projeto = form.cleaned_data['projeto']
            nomeProfessor = form.cleaned_data['nomeProfessor']

            new_form = Disciplina(projeto = projeto, nomeProfessor = nomeProfessor)
            new_form.save()
            form = FormDisciplinaNova()
            context = {
                'form': form
            }
            return render(request,"disciplina/disciplina_form.html", context=context)

def disciplina_list(request):
    disciplinas = Disciplina.objects.all()
    context = {
        'disciplinas': disciplinas,
    }
    return  render(request, "disciplina/disciplina_list.html", context)

class DisciplinaDetail(generic.DetailView):
    model = Disciplina

# class DisciplinaNova(generic.CreateView):
#     model = Disciplina
#     fields = '__all__'

# class DisciplinaLista(generic.ListView):
#     model = Disciplina
#     queryset = Disciplina.objects.all()

# class DisciplinaUpdate(generic.UpdateView):
#     model = Disciplina
#     fields = ['projeto', 'nomeProfessor', 'idProfessor',]
#     template_name_suffix = '_update_form'

class DisciplinaDelete(generic.DeleteView):
    model = Disciplina
    success_url = reverse_lazy('disciplina-lista')