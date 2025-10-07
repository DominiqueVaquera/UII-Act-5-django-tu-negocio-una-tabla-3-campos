from django.db import models

# Create your models here.
# clase Alumno con los campos Nombre, precio y stock
class Dulce(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return f"´{self.nombre} - ${self.precio} - Stock: {self.stock}"
