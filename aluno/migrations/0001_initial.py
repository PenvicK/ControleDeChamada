# Generated by Django 4.0.3 on 2022-04-09 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ra', models.IntegerField()),
                ('nome', models.CharField(max_length=40)),
                ('usuarioDiscord', models.CharField(max_length=20)),
                ('rfID', models.CharField(max_length=30)),
            ],
        ),
    ]
