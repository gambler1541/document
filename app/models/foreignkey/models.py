from django.db import models


class Car(models.Model):
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.ForeignKey('self', on_delete=models.SET_NULL,related_name='student',blank=True, null=True)
