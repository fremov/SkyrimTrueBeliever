# Generated by Django 5.2 on 2025-04-21 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stb_database_app', '0002_alter_races_options_alter_races_armor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InnateAbilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ability', models.CharField(max_length=150, verbose_name='Описание способности')),
            ],
            options={
                'verbose_name': 'Способность',
                'verbose_name_plural': 'Способности',
            },
        ),
    ]
