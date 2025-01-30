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
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    contact = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logos/', blank = True, null= True)
    type_etablissement = models.CharField(max_length=10, choices=TYPE_CHOICES, default='ecole')
    decoupage_annuel = models.CharField(
        max_length=10, 
        choices=DECOUPAGE_CHOICES, 
        default='trimestre'
    )

    def save(self, *args, **kwargs):
        """ Assigner automatiquement le découpage en fonction du type d'établissement """
        if self.type_etablissement == 'universite':
            self.decoupage_annuel = 'semestre'
        else:
            self.decoupage_annuel = 'trimestre'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom
