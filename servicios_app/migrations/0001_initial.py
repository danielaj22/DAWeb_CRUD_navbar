# Generated by Django 5.1 on 2024-12-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('Id_Servicio', models.IntegerField(primary_key=True, serialize=False)),
                ('Id_cliente', models.IntegerField()),
                ('Id_Empleado', models.IntegerField()),
                ('tipo', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=50)),
                ('fecha_serv', models.DateField()),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'db_table': 'Servicios',
            },
        ),
    ]
