from django.db import models

__all__ = (
    'Topping',
    'Pizza',
)
class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(
        Topping,
        related_name='pizzas',

    )

    def __str__(self):
        return self.name


