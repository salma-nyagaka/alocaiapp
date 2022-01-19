from django.db import models


class Game(models.Model):
    """Model to create records for the games"""

    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
    name = models.CharField(blank=False, null=False, max_length=255)
    price = models.FloatField(null=False, blank=False)
    space = models.IntegerField(blank=False, null=False)
