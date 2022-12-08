from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=30)
    parentesco=models.CharField(max_length=30)
    nacimiento=models.DateField(max_length=30)

    def __str__(self):
        return self.nombre


