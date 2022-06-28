from django import forms
from django.core.exceptions import ValidationError

from aluno.models import Aluno
from disciplina.models import Disciplina


class FormDisciplinaNova(forms.Form):
    projeto = forms.CharField(max_length=60)
    nomeProfessor = forms.ModelChoiceField(queryset= Aluno.objects.filter(role="professor"))


    def clean(self):
        super(FormDisciplinaNova, self).clean()

        if 'projeto'in self.cleaned_data and 'nomeProfessor' in self.cleaned_data:
            projeto = self.cleaned_data['projeto']

            if Disciplina.objects.filter(projeto = projeto).exists():
                raise ValidationError("Disciplina já cadastrada")
