from django.db import models
import uuid
 
class paises_detalle(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)
    poblacion = models.IntegerField()
    area = models.FloatField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


 