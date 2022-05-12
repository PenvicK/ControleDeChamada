from datetime import datetime, timedelta, timezone

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic

from aluno.models import Aluno
from aula.models import Aula
from disciplina.models import Disciplina
from presenca.forms import FormPresenca
from presenca.models import Presenca


def presenca_form(request):
    if request.method == "GET":
        form = FormPresenca()
        context = {
            'form': form
        }
        return render(request, 'presenca/presenca_form.html', context=context)
    else:
        form = FormPresenca(request.POST)
        if form.is_valid():
            rfId = form.cleaned_data['rfId']
            aluno = Aluno.objects.filter(rfID=rfId)
            date = datetime.today().date()
            time = datetime.today().time()

            prazo_primeira_aula = datetime(date.year, date.month, date.day, 19, 30, 0).time()
            prazo_segunda_aula = datetime(date.year, date.month, date.day, 20, 30, 0).time()
            prazo_terceira_aula = datetime(date.year, date.month, date.day, 21, 30, 0).time()
            prazo_final_aula = datetime(date.year, date.month, date.day, 22, 30, 0).time()

            primeira_aula = datetime(date.year, date.month, date.day, 19, 0, 0).time()
            segunda_aula = datetime(date.year, date.month, date.day, 20, 0, 0).time()
            terceira_aula = datetime(date.year, date.month, date.day, 21, 0, 0).time()
            final_aula = datetime(date.year, date.month, date.day, 22, 0, 0).time()

            if time < prazo_primeira_aula:
                time = primeira_aula
            elif prazo_primeira_aula < time < prazo_segunda_aula:
                time = segunda_aula
            elif prazo_primeira_aula < time > prazo_segunda_aula and time < prazo_terceira_aula:
                time = terceira_aula
            elif prazo_primeira_aula < time > prazo_segunda_aula and prazo_terceira_aula < time < prazo_final_aula:
                time = final_aula
            else:
                time = datetime.now().time()

            diferenca = timedelta(hours=-3)
            fuso_horario = timezone(diferenca)

            timePrimeiraAula = primeira_aula
            timeSegundaAula = segunda_aula
            timeTerceiraAula = terceira_aula

            date_time_primeira_aula = datetime.combine(date, timePrimeiraAula).astimezone(fuso_horario)
            date_time_segunda_aula = datetime.combine(date, timeSegundaAula).astimezone(fuso_horario)
            date_time_terceira_aula = datetime.combine(date, timeTerceiraAula).astimezone(fuso_horario)

            disciplinaPrimeiraAula = Aula.objects.filter(dataHora=date_time_primeira_aula)
            disciplinaSegundaAula = Aula.objects.filter(dataHora=date_time_segunda_aula)
            disciplinaTerceiraAula = Aula.objects.filter(dataHora=date_time_terceira_aula)


            if time == primeira_aula:
                pre_aula1 = Presenca(aluno=aluno, aula=disciplinaPrimeiraAula, presenca=False, flTemp=True)
                pre_aula2 = Presenca(aluno=aluno, aula=disciplinaSegundaAula, presenca=False, flTemp=True)
                pre_aula3 = Presenca(aluno=aluno, aula=disciplinaTerceiraAula, presenca=False, flTemp=True)
                pre_aula1.save()
                pre_aula2.save()
                pre_aula3.save()
            elif time == segunda_aula:
                pre_aula1 = Presenca(aluno=aluno, aula=disciplinaPrimeiraAula, presenca=False, flTemp=False)
                pre_aula2 = Presenca(aluno=aluno, aula=disciplinaSegundaAula, presenca=False, flTemp=True)
                pre_aula3 = Presenca(aluno=aluno, aula=disciplinaTerceiraAula, presenca=False, flTemp=True)
                pre_aula1.save()
                pre_aula2.save()
                pre_aula3.save()
            elif time == terceira_aula:
                pre_aula1 = Presenca(aluno=aluno, aula=disciplinaPrimeiraAula, presenca=False, flTemp=False)
                pre_aula2 = Presenca(aluno=aluno, aula=disciplinaSegundaAula, presenca=False, flTemp=False)
                pre_aula3 = Presenca(aluno=aluno, aula=disciplinaTerceiraAula, presenca=False, flTemp=True)
                pre_aula1.save()
                pre_aula2.save()
                pre_aula3.save()
            elif time == final_aula:

                if Presenca.objects.filter(aluno=aluno).filter(aula=disciplinaPrimeiraAula).exists() and Presenca.objects.filter(aluno=aluno).filter(aula=disciplinaSegundaAula).exists() and Presenca.objects.filter(aluno=aluno).filter(aula=disciplinaTerceiraAula).exists():
                    pre_aula1 = Presenca.objects.filter(aluno=aluno).filter(aula=disciplinaPrimeiraAula)
                    pre_aula2 = Presenca.objects.filter(aluno=aluno).filter(aula=disciplinaSegundaAula)
                    pre_aula3 = Presenca.objects.filter(aluno=aluno).filter(aula=disciplinaTerceiraAula)
                    if pre_aula1.model.flTemp:
                        pre_aula1.update(presenca=True)
                    if pre_aula2.model.flTemp:
                        pre_aula2.update(presenca=True)
                    if pre_aula3.model.flTemp:
                        pre_aula3.update(presenca=True)

            form = FormPresenca()
            context = {
                'form': form
            }
            return render(request,"presenca/presenca_form.html",context=context)


def presenca_list(request):
    aulas = Aula.objects.all()
    context = {
        'aulas': aulas,
        'timezones': 'America/Sao_Paulo',
    }
    return  render(request, "aula/aula_list.html", context)

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