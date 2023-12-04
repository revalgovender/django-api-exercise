from django.db import models


class Seller(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
