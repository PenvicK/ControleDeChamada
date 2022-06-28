from django.db import models

# Create your models here.
from django.urls import reverse

from aluno.models import Aluno


class Disciplina (models.Model):
    projeto = models.CharField(max_length=60)
    nomeProfessor = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    idProfessor = models.IntegerField(null=True)

    def __str__(self):
        return self.projeto

    def get_absolute_url(self):
        return reverse('aula-nova')