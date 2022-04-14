from django.db import models

# Create your models here.
from django.urls import reverse


class Disciplina (models.Model):
    projeto = models.CharField(max_length=60)
    nomeProfessor = models.CharField(max_length=30)
    idProfessor = models.IntegerField()

    def __str__(self):
        return self.projeto

    def get_absolute_url(self):
        return reverse('aula-nova')