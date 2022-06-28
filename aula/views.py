from datetime import datetime, timezone, timedelta

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from aula.forms import FormAulaNova
from aula.models import Aula


def aula_form(request):
    if request.method == "GET":
        form = FormAulaNova()
        context = {
            'form': form
        }
        return render(request, 'aula/aula_form.html', context=context)
    else:
        form = FormAulaNova(request.POST)
        if form.is_valid():
            date = form.cleaned_data['data']
            disciplina = form.cleaned_data['disciplina']
            periodo = form.cleaned_data['periodo']
            curso = form.cleaned_data['curso']
            diferenca = timedelta(hours=-3)
            fuso_horario = timezone(diferenca)

            if periodo == "N":
                time1 = datetime(date.year, date.month, date.day, 19, 0, 0).time()
                time2 = datetime(date.year, date.month, date.day, 20, 0, 0).time()
                time3 = datetime(date.year, date.month, date.day, 21, 0, 0).time()
            else:
                time1 = datetime(date.year, date.month, date.day, 8, 0, 0).time()
                time2 = datetime(date.year, date.month, date.day, 9, 0, 0).time()
                time3 = datetime(date.year, date.month, date.day, 10, 0, 0).time()

            dataHora1 = datetime.combine(date, time1).astimezone(fuso_horario)
            dataHora2 = datetime.combine(date, time2).astimezone(fuso_horario)
            dataHora3 = datetime.combine(date, time3).astimezone(fuso_horario)

            nmAula= disciplina.projeto + " - " + curso.curso + " - " + curso.periodo_curso
            new_aula1 = Aula(dataHora=dataHora1, disciplina=disciplina, nmAula=nmAula)
            new_aula1.save()
            new_aula2 = Aula(dataHora=dataHora2, disciplina=disciplina, nmAula=nmAula)
            new_aula2.save()
            new_aula3 = Aula(dataHora=dataHora3, disciplina=disciplina, nmAula=nmAula)
            new_aula3.save()
            form = FormAulaNova()
            context = {
                'form': form
            }
            return render(request,"aula/aula_form.html",context=context)


def aula_list(request):
    aulas = Aula.objects.all()
    context = {
        'aulas': aulas,
        'timezones': 'America/Sao_Paulo',
    }
    return  render(request, "aula/aula_list.html", context)

class AulaDetail(generic.DetailView):
    model = Aula

class AulaDelete(generic.DeleteView):
    model = Aula
    success_url = reverse_lazy('aula-lista')