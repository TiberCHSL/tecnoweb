# Generated by Django 4.2.4 on 2024-06-06 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Entrenadores', '0002_modalidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modalidad',
            name='nombre_modalidad',
            field=models.CharField(choices=[('OL', 'Online'), ('PR', 'Presencial')], default='PR', max_length=2, verbose_name='Nombre de la Modalidad'),
        ),
    ]