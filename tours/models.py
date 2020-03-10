from django.db import models

# Create your models here.
class Tour(models.Model):
   name = models.CharField("Nome", max_length=50)
   date = models.DateField("Data")
   full = models.BooleanField("Lotado", default=False)
   city = models.CharField("Cidade", max_length=50)
   vacancy = models.PositiveIntegerField("Vagas")
   sold = models.PositiveIntegerField("Vendidos")
   tour_type = models.CharField("Tipo", max_length=50)
   meeting_point = models.CharField("Ponto de encontro", max_length=50)
