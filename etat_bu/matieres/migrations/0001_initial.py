# Generated by Django 5.1.5 on 2025-01-31 15:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('etablissements', '0005_remove_etablissement_adresse_and_more'),
        ('utilisateurs', '0003_remove_personne_nom_remove_personne_prenom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('strength', models.PositiveIntegerField(default=0)),
                ('class_teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='classes', to='utilisateurs.personne')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='etablissements.etablissement')),
            ],
        ),
    ]
