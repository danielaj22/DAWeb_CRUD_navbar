# Generated by Django 5.1 on 2024-11-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(max_length=60),
        ),
    ]
