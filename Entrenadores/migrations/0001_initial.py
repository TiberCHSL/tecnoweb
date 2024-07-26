# Generated by Django 4.2.4 on 2024-06-05 16:49

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
            name='Entrenador',
            fields=[
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Teléfono')),
                ('rut_en', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='RUT')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=10, verbose_name='Género')),
                ('role', models.CharField(choices=[('E', 'Entrenador')], default='E', max_length=10, verbose_name='Rol de usuario')),
                ('direccion', models.CharField(blank=True, default='No posee', max_length=100, null=True, verbose_name='Direccion')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de usuario')),
            ],
        ),
        migrations.CreateModel(
            name='LugarTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('AL', 'Aire Libre'), ('GY', 'Gimnasio'), ('DO', 'Domicilio')], default='AL', max_length=2, verbose_name='Tipo de lugar')),
                ('entrenadores', models.ManyToManyField(related_name='Lugares_trabajo', to='Entrenadores.entrenador')),
            ],
        ),
        migrations.CreateModel(
            name='Especializacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_esp', models.CharField(choices=[('PI', 'Pilates'), ('YO', 'Yoga'), ('HI', 'Hipertrofia'), ('RS', 'Resistencia'), ('BP', 'Bajada de peso'), ('FU', 'Futbol'), ('AT', 'Atletismo'), ('PA', 'Pliometria'), ('PL', 'Powerlifting')], default='HI', max_length=2, verbose_name='Nombre de especializacion')),
                ('entrenadores', models.ManyToManyField(related_name='Especializacion', to='Entrenadores.entrenador')),
            ],
        ),
        migrations.CreateModel(
            name='Equipamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MA', 'Mancuernas'), ('BA', 'Barra'), ('MQ', 'Maquinas'), ('N/A', 'No Aplica')], default='N/A', max_length=3, verbose_name='Equipamiento disponible')),
                ('entrenadores', models.ManyToManyField(related_name='Equipamiento', to='Entrenadores.entrenador')),
            ],
        ),
        migrations.CreateModel(
            name='Educacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40, verbose_name='Titulo')),
                ('nombre_ins', models.CharField(max_length=40, verbose_name='Nombre de la institución')),
                ('rut_en', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrenadores.entrenador', verbose_name='Rut del entrenador')),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_inicio', models.CharField(choices=[('LU', 'Lunes'), ('MA', 'Martes'), ('MI', 'Miercoles'), ('JU', 'Jueves'), ('VI', 'Viernes'), ('SA', 'Sabado'), ('DO', 'Domingo')], default='LU', max_length=2, verbose_name='Dia de inicio de la semana')),
                ('dia_fin', models.CharField(choices=[('LU', 'Lunes'), ('MA', 'Martes'), ('MI', 'Miercoles'), ('JU', 'Jueves'), ('VI', 'Viernes'), ('SA', 'Sabado'), ('DO', 'Domingo')], default='LU', max_length=2, verbose_name='Dia de inicio de la semana')),
                ('hora_in', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('rut_en', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Entrenadores.entrenador', verbose_name='Rut del entrenador')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Teléfono')),
                ('rut_cl', models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='RUT')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=10, verbose_name='Género')),
                ('role', models.CharField(choices=[('C', 'Cliente')], default='C', max_length=10, verbose_name='Rol de usuario')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de usuario')),
            ],
        ),
    ]
