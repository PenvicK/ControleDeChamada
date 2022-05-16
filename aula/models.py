from datetime import datetime, timedelta, timezone

from django.db import models

# Create your models here.
from django.urls import reverse

from disciplina.models import Disciplina


class Aula (models.Model):
    dataHora = models.DateTimeField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    nmAula = models.CharField(max_length=80, default="")

    def __str__(self):
        diferenca = timedelta(hours=-3)
        fuso_horario = timezone(diferenca)

        return (self.nmAula + " | " + self.dataHora.astimezone(fuso_horario).strftime("%H:%M"))

    def get_absolute_url(self):
        return reverse('aula-nova')