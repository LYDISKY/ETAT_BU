# Generated by Django 5.1.5 on 2025-01-31 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etablissements', '0003_alter_etablissement_type_etablissement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etablissement',
            name='type_etablissement',
            field=models.CharField(choices=[('ecole', 'École'), ('universite', 'Université')], default='ecole', max_length=10),
        ),
    ]
