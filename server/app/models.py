from django.db import models

class Gyms(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    nome = models.CharField(max_length=80)
    sito = models.CharField(max_length=80, null=True)
    lat = models.CharField(max_length=80, null=True)
    long = models.CharField(max_length=80, null=True)
    indirizzo = models.CharField(max_length=80, null=True)
    comune = models.CharField(max_length=80, null=True)
    provincia  = models.CharField(max_length=80, null=True)
    email =  models.CharField(max_length=80, null=True)
    telefono = models.CharField(max_length=80, null=True)
    descrizione = models.TextField(max_length=200, null=True)

    class Meta:
        verbose_name = 'palestra'
        verbose_name_plural = 'palestre'
        db_table = 'Gyms'

    def __str__(self):
        return f'{self.nome}'


class Courses(models.Model):
    id = models.AutoField(primary_key=True,  auto_created=True)
    nome = models.CharField(max_length=80)
    data_inizio = models.DateField(auto_now_add=True)
    data_fine = models.DateField(auto_now=True)
    descrizione = models.CharField(max_length=200)
    docente = models.CharField(max_length=20)
    idGym = models.ForeignKey(Gyms, related_name='corsi', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'corso'
        verbose_name_plural = 'corsi'
        db_table = 'Courses'

    def __str__(self):
        return f'{self.nome}'

