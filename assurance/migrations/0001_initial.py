# Generated by Django 4.0 on 2022-01-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('cne', models.CharField(max_length=50)),
                ('date_naissance', models.DateTimeField()),
                ('telephone', models.CharField(max_length=30)),
                ('Matricule', models.CharField(max_length=100)),
                ('type_contrat', models.CharField(max_length=50)),
                ('num_contrat', models.IntegerField()),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('type_vehicule', models.CharField(max_length=100)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
