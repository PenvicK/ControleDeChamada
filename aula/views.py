from datetime import datetime, timezone, timedelta

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from aula.forms import FormAulaNova
from aula.models import Aula
from disciplina.models import Disciplina


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
            dt = form.cleaned_data['data']
            data = dt.strftime('%y-%m-%d')
            time = form.cleaned_data['time']
            date_time = data + " " + time
            diferenca = timedelta(hours=-3)
            fuso_horario = timezone(diferenca)
            form_dataHora = datetime.strptime(date_time, '%y-%m-%d %H').astimezone(fuso_horario)
            form_disciplina = form.cleaned_data['disciplina']


            new_form = Aula(dataHora=form_dataHora, disciplina=form_disciplina)
            new_form.save()
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

# class AulaLista(generic.ListView):
#     model = Aula
#     queryset = Aula.objects.all()

# class AulaUpdate(generic.UpdateView):
#     model = Aula
#     fields = ['dataHora',]
#     template_name_suffix = '_update_form'
#
class AulaDelete(generic.DeleteView):
    model = Aula
    success_url = reverse_lazy('aula-lista')