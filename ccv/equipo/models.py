from django.db import models

# Create your models here.
class Equipo(models.Model):
    nombre_equipo = models.CharField(max_length=150)
    #grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True)
#     clase = models.ForeignKey(Clase, on_delete=models.SET_NULL, null=True)
#     mision = models.ForeignKey(Mision, on_delete=models.SET_NULL, null=True)

class Meta:
    managed = False
    db_table = 'equipo'