# from django import template

from django.core.exceptions import ValidationError
from django import forms

from aluno.models import Aluno

# register = template.Library()

# @register.filter(name='addclass')
# def addclass(value, arg):
#     return value.as_widget(attrs={'class': arg})
from curso.models import Curso

ROLE = (
    ('professor', 'Professor'),
    ('aluno', 'Aluno')
)


class FormAlunoNovo(forms.Form):
    ra = forms.IntegerField()
    nome = forms.CharField(max_length=40)
    usuarioDiscord = forms.CharField(max_length=20)
    rfID = forms.CharField(max_length=30)
    role = forms.ChoiceField(choices=ROLE)
    # curso = forms.ModelChoiceField(queryset=Cursos.objects.all())

    def clean(self):
        super(FormAlunoNovo, self).clean()

        if 'ra'in self.cleaned_data and 'nome' in self.cleaned_data and 'usuarioDiscord' in self.cleaned_data and 'rfID' in self.cleaned_data and 'role' in self.cleaned_data :
            ra = self.cleaned_data['ra']
            usuarioDiscord = self.cleaned_data['usuarioDiscord']
            rfID = self.cleaned_data['rfID']
            role = self.cleaned_data['role']
            # curso = self.cleaned_data['curso']

            if Aluno.objects.filter(ra = ra).filter(usuarioDiscord = usuarioDiscord).filter(rfID = rfID).exists() \
                    or Aluno.objects.filter(ra = ra).exists() \
                    or Aluno.objects.filter(usuarioDiscord = usuarioDiscord).exists() \
                    or Aluno.objects.filter(rfID = rfID).exists():
                raise ValidationError("Aluno(a) já cadastrado(a)")