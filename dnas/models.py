from django.contrib.postgres.fields import ArrayField
from django.db import models


class Organism(models.Model):
    dna = ArrayField(models.CharField(max_length=200), blank=True)
    mutation = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.dna} - {self.mutation}"
