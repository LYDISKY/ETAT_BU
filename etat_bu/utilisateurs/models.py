from django.db import models
from django.contrib.auth.models import AbstractUser

class Personne(AbstractUser):
    ROLES = [
        ('SECRETAIRE', 'Secrétaire'),
        ('PROFESSEUR', 'Professeur'),
        ('ETUDIANT', 'Étudiant'),
        ('ELEVE', 'Élève'),
    ]
    nom =  models.CharField(max_length=200 , default='')
    prenom = models.CharField(max_length=200, default= '')
    id_eta = models.ForeignKey('etablissements.Etablissement', on_delete=models.CASCADE, null=True, blank=True)
    telephone = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=ROLES)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nom', 'prenom', 'telephone']

    # Ajout des `related_name` pour éviter les conflits
    groups = models.ManyToManyField(
        'auth.Group',
        related_name="personne_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name="personne_permissions",
        blank=True
    )

    def set_password(self, raw_password):
        """Hache et stocke le mot de passe."""
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)

    def __str__(self):
        return f"{self.nom} {self.prenom} - {self.role}"

    
