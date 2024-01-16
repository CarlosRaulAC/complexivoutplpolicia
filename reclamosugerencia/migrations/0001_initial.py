# Generated by Django 4.2.9 on 2024-01-14 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dependencias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReclamoSugerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=10)),
                ('detalle', models.CharField(max_length=200)),
                ('contacto', models.CharField(max_length=10)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('circuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dependencias.circuito')),
                ('subcircuito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dependencias.subcircuito')),
            ],
            options={
                'verbose_name_plural': 'Reclamos y Sugerencias',
            },
        ),
    ]
