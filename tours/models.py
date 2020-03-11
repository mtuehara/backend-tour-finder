from django.db import models

# Create your models here.
class Tour(models.Model):
   name = models.CharField("Nome", max_length=50)
   date = models.DateField("Data")
   full = models.BooleanField("Lotado", default=False)
   city = models.CharField("Cidade", max_length=50)
   capacity = models.PositiveIntegerField("Capacidade")
   available = models.PositiveIntegerField("Disponíveis")
   TOUR_TYPES = (
    ("Natureza", "Natureza"),
    ("Cultural", "Cultural"),
    ("Aventura", "Aventura"))
   tour_type = models.CharField("Tipo", max_length=50, choices=TOUR_TYPES)
   meeting_point = models.CharField("Ponto de encontro", max_length=50)
