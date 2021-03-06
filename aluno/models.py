from django.db import models
from django.urls import reverse

# from cursos.models import Cursos


class Aluno (models.Model):
    ra = models.IntegerField()
    nome = models.CharField(max_length=40)
    usuarioDiscord = models.CharField(max_length=20)
    rfID = models.CharField(max_length=30)
    role = models.CharField(max_length=10, null=True)
    # curso = models.ForeignKey(Cursos, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('aluno-novo')