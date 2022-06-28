
from datetime import datetime, timedelta, timezone


from django import forms
from django.core.exceptions import ValidationError

from aula.models import Aula
from curso.models import Curso
from disciplina.models import Disciplina

PERIODO_CHOICES = (
    ('M', 'Matutino'),
    ('N', 'Noturno')
)

class FormAulaNova(forms.Form):
    data = forms.DateField()
    curso = forms.ModelChoiceField(queryset=Curso.objects.all())
    periodo = forms.ChoiceField(choices=PERIODO_CHOICES)
    disciplina = forms.ModelChoiceField(queryset=Disciplina.objects.all())



    def clean(self):
        super(FormAulaNova, self).clean()

        if 'data'in self.cleaned_data and 'disciplina' in self.cleaned_data and 'periodo' in self.cleaned_data and 'curso' in self.cleaned_data:
            date = self.cleaned_data['data']
            disciplina = self.cleaned_data['disciplina']
            periodo = self.cleaned_data['periodo']
            curso = self.cleaned_data['curso']
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

            nmAula = disciplina.projeto + " - " + curso.curso + " - " + curso.periodo_curso

            if Aula.objects.filter(disciplina = disciplina).filter(dataHora=dataHora1).filter(nmAula=nmAula).exists() or Aula.objects.filter(disciplina = disciplina).filter(dataHora=dataHora2).filter(nmAula=nmAula).exists() or Aula.objects.filter(disciplina = disciplina).filter(dataHora=dataHora3).filter(nmAula=nmAula).exists():
                raise ValidationError("Aula já cadastrada")
