from django.db import models

class IceCream(models.Model):
    FLAVOR_CHOICES = [
        ('vanilla', 'Vanilla'),
        ('chocolate', 'Chocolate'),
        ('strawberry', 'Strawberry'),
        ('mint', 'Mint'),
        ('cookie_dough', 'Cookie Dough'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=20, choices=FLAVOR_CHOICES)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.get_flavor_display()})"
