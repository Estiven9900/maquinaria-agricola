# Generated by Django 5.1.7 on 2025-03-30 13:48

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complemento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('estado', models.CharField(choices=[('activo', 'Activo'), ('inactivo', 'Inactivo'), ('mantenimiento', 'Mantenimiento')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_rol', models.CharField(choices=[('operador', 'Operador'), ('mecanico', 'Mecánico'), ('supervisor', 'Supervisor')], max_length=20)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('pin', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Maquina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('estado_maquina', models.CharField(choices=[('operativa', 'Operativa'), ('averiada', 'Averiada'), ('mantenimiento', 'Mantenimiento')], max_length=20)),
                ('cilindraje', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('modelo', models.CharField(max_length=50)),
                ('serial', models.CharField(max_length=50, unique=True)),
                ('estado_disponible', models.BooleanField(default=True)),
                ('kilometraje', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('tipo_combustible', models.CharField(choices=[('gasolina', 'Gasolina'), ('diesel', 'Diesel'), ('electrico', 'Eléctrico')], max_length=20)),
                ('id_complemento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='maquinaria_agricola.complemento')),
            ],
        ),
        migrations.CreateModel(
            name='Operacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateTimeField()),
                ('fecha_salida', models.DateTimeField(blank=True, null=True)),
                ('area', models.CharField(max_length=50)),
                ('consumo', models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0)])),
                ('observaciones', models.TextField(blank=True)),
                ('id_maquinaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maquinaria_agricola.maquina')),
                ('id_trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maquinaria_agricola.trabajador')),
            ],
        ),
    ]
