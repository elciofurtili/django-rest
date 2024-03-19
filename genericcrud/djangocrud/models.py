from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)