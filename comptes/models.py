from django.contrib.auth.models import AbstractUser
from django.db import models


class Utilisateur(AbstractUser):
    class Role(models.TextChoices):
        COMMISSAIRE = "COMMISSAIRE", "Commissaire de justice"
        CLERC = "CLERC", "Clerc / collaborateur"
        SECRETAIRE = "SECRETAIRE", "Secrétaire"
        COMPTABLE = "COMPTABLE", "Comptable"

    role = models.CharField(max_length=15, choices=Role.choices, default=Role.SECRETAIRE)

# Create your models here.
