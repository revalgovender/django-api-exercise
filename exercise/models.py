from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=100)


class Item(models.Model):
    name = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='items', null=True, blank=True)


class Payout(models.Model):
    seller_reference = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='payouts')
    items = models.ManyToManyField(Item, related_name='payouts', blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)