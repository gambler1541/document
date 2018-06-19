from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)


    def __str__(self):
        return f'[{self.pk}] place({self.name})'

    class Meta:
        ordering = ['name']

class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'[{self.pk}] Restaurant'


class Supplier(Place):
    customers = models.ForeignKey(Place,
                                  on_delete=models.CASCADE,
                                  related_name='supplier_by_customer')

