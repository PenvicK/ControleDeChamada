from django.db import models

# Create your models here.
from django.urls import reverse

from disciplina.models import Disciplina


class Aula (models.Model):
    dataHora = models.DateTimeField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.disciplina.projeto) + str(' | ') + str(self.dataHora.time())

    def get_absolute_url(self):
        return reverse('aula-nova')