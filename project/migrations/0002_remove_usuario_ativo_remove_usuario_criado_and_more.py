# Generated by Django 4.1.1 on 2022-09-17 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='criado',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='modificado',
        ),
    ]
