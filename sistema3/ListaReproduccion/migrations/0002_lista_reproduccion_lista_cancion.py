# Generated by Django 5.0.1 on 2024-02-02 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ListaReproduccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lista_reproduccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ListaReproduccion.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='lista_cancion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cancion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ListaReproduccion.cancion')),
                ('lista_reproduccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ListaReproduccion.lista_reproduccion')),
            ],
        ),
    ]
