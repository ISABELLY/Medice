# Generated by Django 4.0.7 on 2022-08-31 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0002_pacientes'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pacientes',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='login',
            field=models.EmailField(max_length=75),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='senha',
            field=models.CharField(max_length=100),
        ),
    ]
