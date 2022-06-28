from datetime import datetime, timedelta, timezone
from django.http import HttpResponseServerError, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from aluno.models import Aluno
from aula.models import Aula
from presenca.forms import FormPresenca
from presenca.models import Presenca
import json

def discord_post_presenca(request):
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        try:
            nmAula = body['nmAula']
            discordID = body['discordID']
            aluno = Aluno.objects.filter(usuarioDiscord=discordID).get()
            date = datetime.today().date()
            time = datetime.today().time()
            manha = datetime(date.year, date.month, date.day, 7, 30, 0).time()
            noite = datetime(date.year, date.month, date.day, 18, 30, 0).time()
            prazo_final_aula_manha = datetime(date.year, date.month, date.day, 11, 30, 0).time()
            prazo_final_aula_noite = datetime(date.year, date.month, date.day, 22, 30, 0).time()
            if aluno.role != "aluno":
                raise ValueError("Não é um aluno!")
            if prazo_final_aula_manha > time > manha:
                prazo_primeira_aula = datetime(date.year, date.month, date.day, 8, 30, 0).time()
                prazo_segunda_aula = datetime(date.year, date.month, date.day, 9, 30, 0).time()
                prazo_terceira_aula = datetime(date.year, date.month, date.day, 10, 30, 0).time()
                prazo_final_aula = datetime(date.year, date.month, date.day, 11, 30, 0).time()
            if prazo_final_aula_noite > time > noite:
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

            primeiraAula = Aula.objects.filter(dataHora=date_time_primeira_aula).filter(nmAula=nmAula).get()
            segundaAula = Aula.objects.filter(dataHora=date_time_segunda_aula).filter(nmAula=nmAula).get()
            terceiraAula = Aula.objects.filter(dataHora=date_time_terceira_aula).filter(nmAula=nmAula).get()

            isSaved = False
            if Presenca.objects.filter(aluno=aluno).filter(aula=primeiraAula).exists() or Presenca.objects.filter(
                    aluno=aluno).filter(aula=segundaAula).exists() or Presenca.objects.filter(aluno=aluno).filter(
                    aula=terceiraAula).exists():
                isSaved = True

            if not isSaved:
                if time == primeira_aula:
                    pre_aula1 = Presenca(aluno=aluno, aula=primeiraAula, presenca=False, flTemp=True)
                    pre_aula1.save()
                    pre_aula2 = Presenca(aluno=aluno, aula=segundaAula, presenca=False, flTemp=True)
                    pre_aula2.save()
                    pre_aula3 = Presenca(aluno=aluno, aula=terceiraAula, presenca=False, flTemp=True)
                    pre_aula3.save()
                elif time == segunda_aula:
                    pre_aula1 = Presenca(aluno=aluno, aula=primeiraAula, presenca=False, flTemp=False)
                    pre_aula2 = Presenca(aluno=aluno, aula=segundaAula, presenca=False, flTemp=True)
                    pre_aula3 = Presenca(aluno=aluno, aula=terceiraAula, presenca=False, flTemp=True)
                    pre_aula1.save()
                    pre_aula2.save()
                    pre_aula3.save()
                elif time == terceira_aula:
                    pre_aula1 = Presenca(aluno=aluno, aula=primeiraAula, presenca=False, flTemp=False)
                    pre_aula1.save()
                    pre_aula2 = Presenca(aluno=aluno, aula=segundaAula, presenca=False, flTemp=False)
                    pre_aula2.save()
                    pre_aula3 = Presenca(aluno=aluno, aula=terceiraAula, presenca=False, flTemp=True)
                    pre_aula3.save()

                elif time == final_aula:
                    pre_aula1f = Presenca(aluno=aluno, aula=primeiraAula, presenca=False, flTemp=False)
                    pre_aula1f.save()
                    pre_aula2f = Presenca(aluno=aluno, aula=segundaAula, presenca=False, flTemp=False)
                    pre_aula2f.save()
                    pre_aula3f = Presenca(aluno=aluno, aula=terceiraAula, presenca=False, flTemp=False)
                    pre_aula3f.save()
            else:
                pre_aula1 = Presenca.objects.get(aluno=aluno, aula=primeiraAula)
                pre_aula2 = Presenca.objects.get(aluno=aluno, aula=segundaAula)
                pre_aula3 = Presenca.objects.get(aluno=aluno, aula=terceiraAula)
                toUpdate1 = Presenca.objects.filter(aluno=aluno).filter(aula=primeiraAula)
                toUpdate2 = Presenca.objects.filter(aluno=aluno).filter(aula=segundaAula)
                toUpdate3 = Presenca.objects.filter(aluno=aluno).filter(aula=terceiraAula)
                if prazo_segunda_aula > datetime.now().time() > prazo_primeira_aula:
                    if pre_aula1.model.flTemp:
                        toUpdate1.update(presenca=True)
                elif prazo_terceira_aula > datetime.now().time() > prazo_segunda_aula:
                    if pre_aula1.model.flTemp:
                        toUpdate1.update(presenca=True)
                    if pre_aula2.model.flTemp:
                        toUpdate2.update(presenca=True)
                elif prazo_final_aula > datetime.now().time() > prazo_terceira_aula:
                    if pre_aula1.flTemp:
                        toUpdate1.update(presenca=True)
                    if pre_aula2.flTemp:
                        toUpdate2.update(presenca=True)
                    if pre_aula3.flTemp:
                        toUpdate3.update(presenca=True)
            return JsonResponse(body)
        except KeyError:
            return HttpResponseServerError("Malformed data!")

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
            aulas = form.cleaned_data['nmAula']
            nmAula = aulas.nmAula
            aluno = Aluno.objects.filter(rfID=rfId).get()
            date = datetime.today().date()
            time = datetime.today().time()
            manha = datetime(date.year, date.month, date.day, 7, 30, 0).time()
            noite = datetime(date.year, date.month, date.day, 18, 30, 0).time()
            prazo_final_aula_manha = datetime(date.year, date.month, date.day, 11, 30, 0).time()
            prazo_final_aula_noite = datetime(date.year, date.month, date.day, 22, 30, 0).time()
            if aluno.role != "aluno":
                raise ValueError("Não é um aluno!")
            if prazo_final_aula_manha > time > manha:
                prazo_primeira_aula = datetime(date.year, date.month, date.day, 8, 30, 0).time()
                prazo_segunda_aula = datetime(date.year, date.month, date.day, 9, 30, 0).time()
                prazo_terceira_aula = datetime(date.year, date.month, date.day, 10, 30, 0).time()
                prazo_final_aula = datetime(date.year, date.month, date.day, 11, 30, 0).time()
            if prazo_final_aula_noite > time > noite:
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

            primeiraAula = Aula.objects.filter(dataHora=date_time_primeira_aula).filter(nmAula=nmAula).get()
            segundaAula = Aula.objects.filter(dataHora=date_time_segunda_aula).filter(nmAula=nmAula).get()
            terceiraAula = Aula.objects.filter(dataHora=date_time_terceira_aula).filter(nmAula=nmAula).get()

            isSaved = False
            if Presenca.objects.filter(aluno=aluno).filter(aula=primeiraAula).exists() or Presenca.objects.filter(aluno=aluno).filter(aula=segundaAula).exists() or Presenca.objects.filter(aluno=aluno).filter(aula=terceiraAula).exists():
                isSaved = True

            if not isSaved:
                if time == primeira_aula:
                    pre_aula1 = Presenca(aluno=aluno, aula=primeiraAula, presenca=False, flTemp=True)
                    pre_aula1.save()
                    pre_aula2 = Presenca(aluno=aluno, aula=segundaAula, presenca=False, flTemp=True)
                    pre_aula2.save()
                    pre_aula3 = Presenca(aluno=aluno, aula=terceiraAula, presenca=False, flTemp=True)
                    pre_aula3.save()
                elif time == segunda_aula:
                    pre_aula1 = Presenca(aluno=aluno, aula=primeiraAula, presenca=False, flTemp=False)
                    pre_aula2 = Presenca(aluno=aluno, aula=segundaAula, presenca=False, flTemp=True)
                    pre_aula3 = Presenca(aluno=aluno, aula=terceiraAula, presenca=False, flTemp=True)
                    pre_aula1.save()
                    pre_aula2.save()
                    pre_aula3.save()
                elif time == terceira_aula:
                    pre_aula1 = Presenca(aluno=aluno, aula=primeiraAula, presenca=False, flTemp=False)
                    pre_aula1.save()
                    pre_aula2 = Presenca(aluno=aluno, aula=segundaAula, presenca=False, flTemp=False)
                    pre_aula2.save()
                    pre_aula3 = Presenca(aluno=aluno, aula=terceiraAula, presenca=False, flTemp=True)
                    pre_aula3.save()

                elif time == final_aula:
                    pre_aula1f = Presenca(aluno=aluno, aula=primeiraAula, presenca=False, flTemp=False)
                    pre_aula1f.save()
                    pre_aula2f = Presenca(aluno=aluno, aula=segundaAula, presenca=False, flTemp=False)
                    pre_aula2f.save()
                    pre_aula3f = Presenca(aluno=aluno, aula=terceiraAula, presenca=False, flTemp=False)
                    pre_aula3f.save()
            else:
                pre_aula1 = Presenca.objects.get(aluno=aluno, aula=primeiraAula)
                pre_aula2 = Presenca.objects.get(aluno=aluno, aula=segundaAula)
                pre_aula3 = Presenca.objects.get(aluno=aluno, aula=terceiraAula)
                toUpdate1 = Presenca.objects.filter(aluno=aluno).filter(aula=primeiraAula)
                toUpdate2 = Presenca.objects.filter(aluno=aluno).filter(aula=segundaAula)
                toUpdate3 = Presenca.objects.filter(aluno=aluno).filter(aula=terceiraAula)
                if  prazo_segunda_aula > datetime.now().time() > prazo_primeira_aula:
                    if pre_aula1.model.flTemp:
                        toUpdate1.update(presenca=True)
                elif prazo_terceira_aula > datetime.now().time() > prazo_segunda_aula:
                    if pre_aula1.model.flTemp:
                        toUpdate1.update(presenca=True)
                    if pre_aula2.model.flTemp:
                        toUpdate2.update(presenca=True)
                elif prazo_final_aula > datetime.now().time() > prazo_terceira_aula:
                    if pre_aula1.flTemp:
                        toUpdate1.update(presenca=True)
                    if pre_aula2.flTemp:
                        toUpdate2.update(presenca=True)
                    if pre_aula3.flTemp:
                        toUpdate3.update(presenca=True)
            form = FormPresenca()
            context = {
                'form': form
            }
            return render(request,"presenca/presenca_form.html",context=context)


def presenca_list(request):
    presencas = Presenca.objects.all()
    context = {
        'presencas': presencas
    }
    return render(request, "presenca/presenca_list.html", context)

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