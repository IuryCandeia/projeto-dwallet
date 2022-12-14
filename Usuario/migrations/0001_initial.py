# Generated by Django 4.1.1 on 2022-10-11 19:22

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('criado', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Criação')),
                ('modificado', models.DateTimeField(auto_now=True, null=True, verbose_name='Data de Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('genero', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino'), ('o', 'Outros')], max_length=100, verbose_name='Sexo')),
                ('telefone', models.CharField(blank=True, default='', max_length=21, null=True, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
