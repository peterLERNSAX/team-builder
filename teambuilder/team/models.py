from django.db import models

class Player(models.Model):
    """
    Model for a player
    """
    name = models.CharField(max_length=200,null=False)
    birthdate = models.DateField(null=True)
    position = models.CharField(max_length=3,null=True)
    gender = models.CharField(max_length=3,null=True)
    comment = models.CharField(max_length=1000,null=True)
    image = models.TextField(null=True) #Base64 string
