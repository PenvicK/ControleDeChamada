from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from aluno.forms import FormAlunoNovo
from aluno.models import Aluno

def aluno_form(request):
    if request.method == "GET":
        form = FormAlunoNovo()
        context = {
            'form': form
        }
        return render(request, 'aluno/aluno_form.html', context=context)
    else:
        form = FormAlunoNovo(request.POST)
        if form.is_valid():
            ra = form.cleaned_data['ra']
            nome = form.cleaned_data['nome']
            userDisc = form.cleaned_data['usuarioDiscord']
            rfID = form.cleaned_data['rfID']

            new_form = Aluno(ra = ra, nome = nome, usuarioDiscord = userDisc, rfID = rfID)
            new_form.save()
            form = FormAlunoNovo()
            context = {
                'form': form
            }
            return render(request,"aluno/aluno_form.html", context=context)


class AlunoDetail(generic.DetailView):
    model = Aluno

# class AlunoNovo(generic.CreateView):
#     model = Aluno
#     fields = '__all__'

# class AlunoLista(generic.ListView):
#     model = Aluno
#     queryset = Aluno.objects.all()

def aluno_list(request):
    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos,
    }
    return  render(request, "aluno/aluno_list.html", context)

# class AlunoUpdate(generic.UpdateView):
#     model = Aluno
#     fields = ['nome','usuarioDiscord', 'rfID',]
#     template_name_suffix = '_update_form'

class AlunoDelete(generic.DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno-lista')