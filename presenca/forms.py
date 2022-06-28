from datetime import datetime, timedelta, timezone

from django import forms
from django.core.exceptions import ValidationError

from aluno.models import Aluno
from aula.models import Aula
from disciplina.models import Disciplina
from presenca.models import Presenca

PRESENCA_CHOICES = (
    ('true', 'Presente'),
    ('false', 'Ausente'),
)


class FormPresenca(forms.Form):
    rfId = forms.CharField(max_length=30)
    nmAula = forms.ModelChoiceField(queryset=Aula.objects.all())

    def clean(self):
        super(FormPresenca, self).clean()

        if 'rfId' in self.cleaned_data and 'nmAula' in self.cleaned_data:
            rfId = self.cleaned_data['rfId']
            aulas = self.cleaned_data['nmAula']
            nmAula = aulas.nmAula
            if Aluno.objects.filter(rfID=rfId).exists():
                aluno = Aluno.objects.filter(rfID=rfId)
                date = datetime.today().date()
                time = datetime.today().time()

                prazo_inicio_aula = datetime(date.year, date.month, date.day, 18, 30, 0).time()
                prazo_primeira_aula = datetime(date.year, date.month, date.day, 19, 30, 0).time()
                prazo_segunda_aula = datetime(date.year, date.month, date.day, 20, 30, 0).time()
                prazo_terceira_aula = datetime(date.year, date.month, date.day, 21, 30, 0).time()
                prazo_final_aula = datetime(date.year, date.month, date.day, 22, 50, 0).time()

                primeira_aula = datetime(date.year, date.month, date.day, 19, 0, 0).time()
                segunda_aula = datetime(date.year, date.month, date.day, 20, 0, 0).time()
                terceira_aula = datetime(date.year, date.month, date.day, 21, 0, 0).time()
                final_aula = datetime(date.year, date.month, date.day, 22, 0, 0).time()

                if prazo_primeira_aula > time > prazo_inicio_aula:  # tempo menor que prazo primeira aula
                    time = primeira_aula
                elif prazo_primeira_aula < time < prazo_segunda_aula:  # tempo maior que prazo primeira aula & menor que segunda aula
                    time = segunda_aula
                elif prazo_primeira_aula < time > prazo_segunda_aula and time < prazo_terceira_aula:  # tempo maior que prazo primeira aula, segunda aula & menor que terceira aula
                    time = terceira_aula
                elif prazo_primeira_aula < time > prazo_segunda_aula and prazo_terceira_aula < time < prazo_final_aula:  # tempo maior que prazo primeira aula, segunda aula, terceira aula & menor que final aula
                    time = final_aula
                else:
                    time = datetime.now().time()

                diferenca = timedelta(hours=-3)
                fuso_horario = timezone(diferenca)
                date_time = datetime.combine(date, time).astimezone(fuso_horario)

                if time > prazo_final_aula:
                    raise ValueError("Você está Atrasado!")
                if time < prazo_inicio_aula:
                    raise ValueError("Chamada não iniciada!")
                if Aula.objects.filter(dataHora=date_time).filter(nmAula=nmAula) is None:
                    raise ValueError("Disciplina não encontrada!")


