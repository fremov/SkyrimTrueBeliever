# Generated by Django 5.2 on 2025-04-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stb_database_app', '0006_daedra'),
    ]

    operations = [
        migrations.AddField(
            model_name='daedra',
            name='daedrea_influence',
            field=models.CharField(default='', verbose_name='Сфера влияния даэдра'),
        ),
        migrations.AddField(
            model_name='daedra',
            name='quest',
            field=models.CharField(default='', verbose_name='Квест'),
        ),
        migrations.AddField(
            model_name='daedra',
            name='quest_url',
            field=models.CharField(default='', verbose_name='Ссылка на квест'),
        ),
    ]
