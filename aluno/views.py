from django.core import serializers
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from aluno.forms import FormAlunoNovo
from aluno.models import Aluno
import json
from django.http import HttpResponse, Http404


def some_view(request, nickName, id):
    discordID = nickName + "#" + id
    if not Aluno.objects.filter(usuarioDiscord = discordID).exists():
        qs = Aluno.objects.filter(usuarioDiscord="NOTFOUND#123")
        qs_json = serializers.serialize('json', qs)
        return HttpResponse(qs_json, content_type='application/json')
    else:
        qs = Aluno.objects.filter(usuarioDiscord=discordID)
        qs_json = serializers.serialize('json', qs)
        return HttpResponse(qs_json, content_type='application/json')



# def getByDiscordUser(request,usuarioDiscord):
#     response = get_object_or_404(Aluno, usuarioDiscord = usuarioDiscord)
#     # response_data = Aluno.objects.filter(usuarioDiscord = usuarioDiscord).exists()
#
#     return HttpResponse(json.dumps(response), content_type="application/json")
# def getAll(request):
#     response = Aluno.objects.all()
#     # response_data = Aluno.objects.filter(usuarioDiscord = usuarioDiscord).exists()
#
#     if not response:
#         raise Http404("No response matches the given query.")


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
            role = form.cleaned_data['role']
            # curso = form.cleaned_data['curso']

            new_form = Aluno(ra=ra, nome=nome, usuarioDiscord=userDisc, rfID=rfID, role=role)
            new_form.save()
            form = FormAlunoNovo()
            context = {
                'form': form
            }
            return render(request, "aluno/aluno_form.html", context=context)

def professor_form(request):
    if request.method == "GET":
        form = FormAlunoNovo()
        context = {
            'form': form
        }
        return render(request, 'professor/professor_form.html', context=context)
    else:
        form = FormAlunoNovo(request.POST)
        if form.is_valid():
            ra = form.cleaned_data['ra']
            nome = form.cleaned_data['nome']
            userDisc = form.cleaned_data['usuarioDiscord']
            rfID = form.cleaned_data['rfID']
            role = form.cleaned_data['role']

            new_form = Aluno(ra=ra, nome=nome, usuarioDiscord=userDisc, rfID=rfID, role=role)
            new_form.save()
            form = FormAlunoNovo()
            context = {
                'form': form
            }
            return render(request, "professor/professor_form.html", context=context)

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
    return render(request, "aluno/aluno_list.html", context)

def professor_list(request):
    alunos = Aluno.objects.all()
    context = {
        'alunos': alunos,
    }
    return render(request, "professor/professor_list.html", context)
# class AlunoUpdate(generic.UpdateView):
#     model = Aluno
#     fields = ['nome','usuarioDiscord', 'rfID',]
#     template_name_suffix = '_update_form'

class AlunoDelete(generic.DeleteView):
    model = Aluno
    success_url = reverse_lazy('aluno-lista')
