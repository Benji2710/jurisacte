from django.conf import settings
from django.db import models


class Evenement(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="+",
    )
    action = models.CharField(max_length=40)      # ex. CREATION, MODIFICATION, VALIDATION
    objet = models.CharField(max_length=120)      # ex. "Acte 2026-0012"
    detail = models.TextField(blank=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.date:%d/%m/%Y %H:%M} {self.action} {self.objet}"