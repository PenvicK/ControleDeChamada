from datetime import datetime, timedelta, timezone

from django import forms
from django.core.exceptions import ValidationError

from aluno.models import Aluno
from disciplina.models import Disciplina
from presenca.models import Presenca

PRESENCA_CHOICES = (
    ('true', 'Presente'),
    ('false', 'Ausente'),
)
class FormPresenca(forms.Form):
    rfId = forms.CharField(max_length=30)

    def clean(self):
        super(FormPresenca, self).clean()

        if 'rfId'in self.cleaned_data:
            rfId = self.cleaned_data['rfId']
            if Aluno.objects.filter(rfID = rfId).exists():
                aluno = Aluno.objects.filter(rfID = rfId)
                date = datetime.today()
                time = datetime.now().time()

                prazo_primeira_aula = datetime.time(19,30,00)
                prazo_segunda_aula = datetime.time(20,30,00)
                prazo_terceira_aula = datetime.time(21,30,00)
                prazo_final_aula = datetime.time(22,30,00)

                primeira_aula = datetime.time(19, 00, 00)
                segunda_aula = datetime.time(20, 00, 00)
                terceira_aula = datetime.time(21, 00, 00)
                final_aula = datetime.time(22, 00, 00)

                if time < prazo_primeira_aula:
                    time = datetime.time(primeira_aula)
                elif time > prazo_primeira_aula and time < prazo_segunda_aula:
                    time = datetime.time(segunda_aula)
                elif time > prazo_primeira_aula and time > prazo_segunda_aula and time < prazo_terceira_aula:
                    time = datetime.time(terceira_aula)
                elif time > prazo_primeira_aula and time > prazo_segunda_aula and time > prazo_terceira_aula and time < prazo_final_aula:
                    time = datetime.time(final_aula)
                else:
                    time = datetime.now().time()

                diferenca = timedelta(hours=-3)
                fuso_horario = timezone(diferenca)
                date_time = datetime.combine(date,time).astimezone(fuso_horario)

                if Disciplina.objects.filter(datetime = date_time).exists():
                    disciplina = Disciplina.objects.filter(datetime=date_time)
                    if Presenca.objects.filter(disciplina = disciplina, aluno = aluno):
                        raise ValidationError("Aluno já presente")
                if Disciplina.objects.filter(datetime = date_time).none() or time > prazo_final_aula:
                    if time > prazo_final_aula:
                        raise ValidationError("Você está Atrasado!")
                    else:
                        raise ValidationError("Disciplina não encontrada")
