from django.db import models

class Etablissement(models.Model):

    TYPE_CHOICES = [
        ('ecole', 'École'),
        ('universite', 'Université'),
    ]

    DECOUPAGE_CHOICES = [
        ('trimestre', 'Trimestre'),
        ('semestre', 'Semestre'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField("Nom",max_length=255, default="")
    code = models.CharField(max_length=255, default="")
    address = models.TextField("Adresse",max_length=300, default="")
    contact = models.CharField(max_length=20,)
    logo = models.ImageField(upload_to='logos/', blank = True, null= True)
    type_etablissement = models.CharField(max_length=10, choices=TYPE_CHOICES, default='ecole')
    decoupage_annuel = models.CharField(max_length=10, choices=DECOUPAGE_CHOICES, default='trimestre')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
