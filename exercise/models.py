from django.db import models


class Seller(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Items(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Payouts(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    seller_id = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='payouts')
    seller_reference = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ItemPayout(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    payout_id = models.ForeignKey(Payouts, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Items, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
