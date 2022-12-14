# Generated by Django 4.1.1 on 2022-10-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Financa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='', max_length=100, verbose_name='Título')),
                ('descricao', models.CharField(default='', max_length=1024, verbose_name='Descrição')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor')),
            ],
        ),
    ]
