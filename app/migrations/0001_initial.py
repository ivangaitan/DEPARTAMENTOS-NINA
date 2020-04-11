# Generated by Django 2.1 on 2020-04-06 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('residencia', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alquilado', models.BooleanField()),
                ('inicio_alquiler', models.DateTimeField(auto_now=True)),
                ('fin_alquiler', models.DateTimeField()),
                ('calle', models.CharField(max_length=20)),
                ('altura', models.CharField(max_length=4)),
                ('edificio', models.CharField(max_length=20)),
                ('piso', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
    ]
