# Generated by Django 4.0.7 on 2022-08-22 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=200)),
                ('senha', models.FloatField(max_length=30)),
                ('nome', models.CharField(max_length=30)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
