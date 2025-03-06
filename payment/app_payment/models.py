# from django.db import models
#
# # Create your models here.
# from django.db import models
#
# class Item(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.IntegerField()
#     currency = models.CharField(max_length=3, choices=[('usd', 'USD'), ('eur', 'EUR')])
#
#     def __str__(self):
#         return self.name
#
#
# class Order(models.Model):
#     items = models.ManyToManyField(Item)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def total_price(self):
#         return sum(item.price for item in self.items.all())
#
#     class Discount(models.Model):
#         name = models.CharField(max_length=255)
#         percentage = models.FloatField()
#
#     class Tax(models.Model):
#         name = models.CharField(max_length=255)
#         percentage = models.FloatField()
#
#
# from django.db import models
#
# class Item(models.Model):
#     CURRENCIES = [('usd', 'USD'), ('eur', 'EUR')]
#
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     currency = models.CharField(max_length=3, choices=CURRENCIES, default='usd')
#
#     def get_price_cents(self):
#         return int(self.price * 100)
#
#     def __str__(self):
#         return f"{self.name} ({self.currency()})"
from django.db import models

class Item(models.Model):
    CURRENCIES = [('usd', 'USD'), ('eur', 'EUR')]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=CURRENCIES, default='usd')

    def get_price_cents(self):
        return int(self.price * 100)

    def __str__(self):
        return f"{self.name} ({self.currency.upper()})"


