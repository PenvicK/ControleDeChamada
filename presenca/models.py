from django.db import models

# Create your models here.
from django.urls import reverse

from aluno.models import Aluno
from aula.models import Aula


class Presenca (models.Model):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    presenca = models.BooleanField(null=True)
    flTemp = models.BooleanField(null=True)

    def __str__(self):
        return str(self.aluno.nome)

    def et_absolute_url(self):
        return reverse('presenca-nova')