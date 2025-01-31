from django.db import models
from etablissements.models import Etablissement
from matieres.models import Classe
from utilisateurs.models import Personne

class Bulletin(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="bulletins")  
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="bulletins")  
    etablissement = models.ForeignKey(Etablissement, on_delete=models.CASCADE, related_name="bulletins")  
    period = models.CharField(max_length=20, choices=[  
        ('trimestre_1', 'Premier Trimestre'),
        ('trimestre_2', 'Deuxième Trimestre'),
        ('trimestre_3', 'Troisième Trimestre'),
        ('semestre_1', 'Premier Semestre'),
        ('semestre_2', 'Deuxième Semestre'),
        ('annuel', 'Annuel')
    ])
    moyenne_generale = models.FloatField(default=0.0)  
    appreciation = models.TextField(blank=True, null=True)  
    date_created = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Bulletin de {self.student.nom} - {self.get_period_display()} ({self.etablissement.nom})"

    class Meta:
        unique_together = ('student', 'period', 'etablissement')
