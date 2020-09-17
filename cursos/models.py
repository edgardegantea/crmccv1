from django.db import models


# Create your models here.
class Cursos(models.Model):
    name = models.CharField(verbose_name='Nombre del curso:', unique=True, max_length=200)
    description = models.TextField(verbose_name='Descripción del curso')
    duration = models.PositiveSmallIntegerField(verbose_name='Duración en horas:')
    url = models.URLField(verbose_name='URL del curso')

    def __str__(self):
        return "{0} -> {1}".format(self.duration, self.name)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Competencias(models.Model):
    name = models.CharField(verbose_name='Competencia', unique=True, max_length=255)

    def __str__(self):
        return "{0}".format(self.name)

    class Meta:
        verbose_name = 'Competencia'
        verbose_name_plural = 'Competencias'
