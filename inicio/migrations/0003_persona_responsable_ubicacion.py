# Generated by Django 4.2.2 on 2023-06-29 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_gato_fecha_nacimiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='persona_responsable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_persona', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('dni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ubicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=15)),
                ('codigo_postal', models.IntegerField()),
            ],
        ),
    ]