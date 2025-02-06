from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


class Personne(AbstractUser):
    ROLES = [
        ('SECRETAIRE', 'Secrétaire'),
        ('PROFESSEUR', 'Professeur'),
        ('ETUDIANT', 'Étudiant'),
        ('ELEVE', 'Élève'),
    ] 
    id = models.AutoField(primary_key=True)
    last_name = models.CharField("Nom", max_length=200, default='')
    first_name = models.CharField("Prénom", max_length=200, default='')
    email = models.EmailField("Email", max_length=300, unique=True)
    id_eta = models.ForeignKey('etablissements.Etablissement', on_delete=models.CASCADE, null=True, blank=True)
    tel = models.CharField("Téléphone", max_length=15, unique=True, default='')
    role = models.CharField("Rôle", max_length=20, choices=ROLES)
    password = models.CharField("Mot de passe", max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['last_name', 'first_name']

    # Utiliser `first_name` comme `username`
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)

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

    def save(self, *args, **kwargs):
        """Utilise `first_name` comme `username`, en garantissant l’unicité"""
        if not self.username:
            base_username = slugify(self.first_name)  # Convertir en format URL-friendly
            unique_username = base_username
            counter = 1

            # Vérifier si le username existe déjà
            while Personne.objects.filter(username=unique_username).exists():
                unique_username = f"{base_username}{counter}"
                counter += 1

            self.username = unique_username
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.last_name} {self.first_name} - {self.role}"

    def set_password(self, raw_password):
        """Hache et stocke le mot de passe."""
        from django.contrib.auth.hashers import make_password
        self.password = make_password(raw_password)


    
