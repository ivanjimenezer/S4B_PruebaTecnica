# Generated by Django 5.0.7 on 2024-07-19 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_paises_detalle'),
    ]

    operations = [
        migrations.AddField(
            model_name='paises_detalle',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
