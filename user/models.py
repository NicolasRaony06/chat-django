from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=35)

    def __str__(self):
        return self.username

