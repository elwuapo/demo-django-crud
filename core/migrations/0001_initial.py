# Generated by Django 3.2.3 on 2021-05-28 10:10

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=99)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('nro_chip', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=99)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to=core.models.Perro.ruta_imagen)),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.raza')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ultima_adopcion', models.DateField()),
                ('fecha_login', models.DateTimeField()),
                ('notificar', models.BooleanField()),
                ('perros_adoptados', models.ManyToManyField(to='core.Perro')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]