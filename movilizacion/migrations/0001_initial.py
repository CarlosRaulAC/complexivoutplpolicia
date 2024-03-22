# Generated by Django 4.2.9 on 2024-03-22 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personal', '0001_initial'),
        ('dependencias', '0001_initial'),
        ('flota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movilizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(max_length=50)),
                ('fecha_salida', models.DateTimeField()),
                ('hora', models.TimeField()),
                ('ruta', models.CharField(max_length=50)),
                ('kilometraje', models.CharField(max_length=20)),
                ('numero_ocupantes', models.IntegerField()),
                ('datos_ocupantes', models.CharField(max_length=250)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('estado', models.BooleanField(default=False)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movilizacion_conductor', to='personal.personal')),
                ('solicitante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movilizacion_solicitante', to='personal.personal')),
                ('subcircuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dependencias.subcircuito')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flota.flotavehicular')),
            ],
            options={
                'verbose_name_plural': 'Movilizaciones',
            },
        ),
    ]