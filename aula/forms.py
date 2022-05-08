from datetime import datetime, timedelta, timezone

from django import forms
from django.core.exceptions import ValidationError

from aula.models import Aula
from disciplina.models import Disciplina

HORA_CHOICES = (
    ('19', '19h'),
    ('20', '20h'),
    ('21', '21h')
)


class FormAulaNova(forms.Form):
    data = forms.DateField()
    time = forms.ChoiceField(choices=HORA_CHOICES)
    disciplina = forms.ModelChoiceField(queryset= Disciplina.objects.all())

    def clean(self):
        super(FormAulaNova, self).clean()

        if 'data'in self.cleaned_data and 'time' in self.cleaned_data and 'disciplina' in self.cleaned_data:
            data = self.cleaned_data['data']
            time = self.cleaned_data['time']
            disciplina = self.cleaned_data['disciplina']
            timeConverted = datetime.strptime(time, '%H').time()
            diferenca = timedelta(hours=-3)
            fuso_horario = timezone(diferenca)
            dataHora = datetime.combine(data, timeConverted).astimezone(fuso_horario)
            teste = Aula.objects.filter(disciplina = disciplina).filter(dataHora=dataHora).exists()
            if Aula.objects.filter(disciplina = disciplina).filter(dataHora=dataHora).exists():
                raise ValidationError("Aula já cadastrada")
