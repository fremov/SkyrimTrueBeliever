from django.db import models
from django.db.models import IntegerField


# Create your models here.
class Races(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название расы")
    armor = models.IntegerField(default=0, verbose_name="Броня")
    fire_res = models.IntegerField(default=0, verbose_name="Резист к огню")
    cold_res = models.IntegerField(default=0, verbose_name="Резист к холоду")
    lighting_res = models.IntegerField(default=0, verbose_name="Резист к молнии")
    chaos_res = models.IntegerField(default=0, verbose_name="Резист к хаосу")

    class Meta:
        verbose_name = 'Расу'
        verbose_name_plural = 'Расы'


    def __str__(self):
        return self.title