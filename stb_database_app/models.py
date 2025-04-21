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


class InnateAbilities(models.Model):
    ability = models.CharField(max_length=150, verbose_name="Описание способности")

    class Meta:
        verbose_name = 'Способность'
        verbose_name_plural = 'Способностей'

    def __str__(self):
        return self.ability


class Stones(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название камня силы')
    text = models.TextField(verbose_name='Описание камня силы')
    stone_type = models.CharField(verbose_name='Тип камня силы')

    class Meta:
        verbose_name = 'Камень силы'
        verbose_name_plural = 'Камни силы'

    def __str__(self):
        return self.title


class Aedra(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя бога')
    divine_gift = models.CharField(verbose_name='Божественный дар')
    bless = models.CharField(verbose_name='Благословение')
    amulet = models.CharField(verbose_name='Амулет аэдра')
    backpack_with_amulet = models.CharField('Рюкзак с амулетом аэдра')

    class Meta:
        verbose_name = 'Аэдра'

    def __str__(self):
        return self.name


class Daedra(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя бога')
    divine_gift = models.CharField(verbose_name='Божественный дар')
    artefact = models.CharField(verbose_name='Артефакт')
    effect = models.CharField(verbose_name='Благословение')
    quest = models.CharField(default='', verbose_name='Квест')
    quest_url = models.CharField(default='', verbose_name='Ссылка на квест')
    daedrea_influence = models.CharField(default='', verbose_name='Сфера влияния даэдра')

    class Meta:
        verbose_name = 'Даэдра'

    def __str__(self):
        return self.name
