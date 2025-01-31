from django.db import models
from etablissements.models import Etablissement
from utilisateurs.models import Personne

class Classe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  
    code = models.CharField(max_length=10, unique=True)  
    strength = models.PositiveIntegerField(default=0)  # Number of students 
    institution = models.ForeignKey('etablissements.Etablissement', on_delete=models.CASCADE, related_name="classes")
    class_teacher = models.ForeignKey('utilisateurs.Personne', on_delete=models.SET_NULL, null=True, blank=True, related_name="classes")  # Teacher of the class

    def __str__(self):
        return f"{self.sigle} - {self.name} ({self.institution.nom})"

class Matiere(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  
    code = models.CharField(max_length=10, unique=True)  # Code de la matière (ex: MATH101)
    coefficient = models.PositiveIntegerField(default=1)  
    institution = models.ForeignKey(Etablissement, on_delete=models.CASCADE, related_name="subjects") 
    teacher = models.ForeignKey(Personne, on_delete=models.SET_NULL, null=True, blank=True, related_name="subjects")  

    def __str__(self):
        return f"{self.name} ({self.code})"



class Notation(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Personne, on_delete=models.CASCADE, related_name="grades") 
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, related_name="grades") 
    class_assigned = models.ForeignKey(Classe, on_delete=models.CASCADE, related_name="grades")  # Classe de l'élève
    score = models.FloatField() 
    max_score = models.FloatField(default=20)  # Note maximale possible (par défaut sur 20)
    evaluation_type = models.CharField(max_length=50, choices=[ 
        ('test', 'Test'),
        ('exam', 'Exam'),
        ('assignment', 'Assignment'),
        ('participation', 'Participation')
    ], default='test')
    date_added = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.student.nom} - {self.matiere.name} ({self.score}/{self.max_score})"

    class Meta:
        unique_together = ('student', 'matiere', 'evaluation_type', 'date_added') #Pour eviter les doublons sur la note 
