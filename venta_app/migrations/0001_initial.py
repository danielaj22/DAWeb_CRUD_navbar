# Generated by Django 5.1 on 2024-12-03 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('fecha_venta', models.CharField(max_length=30)),
                ('id_venta', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('id_empleado', models.CharField(max_length=45)),
                ('id_cliente', models.IntegerField()),
                ('id_producto', models.IntegerField()),
                ('cantidad', models.CharField(max_length=6)),
                ('precio_unitario', models.IntegerField()),
                ('forma_pago', models.CharField(max_length=45)),
            ],
        ),
    ]