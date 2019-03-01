from django.db import models

# Create your models here.

class TipoPlan(models.Model):
    nombre = models.CharField(max_length=50)
    costo = models.IntegerField()



class Plan(models.Model):
	tipo = models.ForeignKey(TipoPlan,null=True,blank=True,on_delete=models.CASCADE)
