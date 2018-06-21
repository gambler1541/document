from django.db import models


class PersonManager(models.Manager):
    def create_admin(self, name):
        return self.create(name=name, is_admin=True)


class Person(models.Model):
    name = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)

    objects = PersonManager()

    def __str__(self):
        return f'Person ({self.name})'


class AdminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


class Admin(Person):
    objects = AdminManager()
    class Meta:
        proxy = True

    def delete_user(self, user):
        user.delete()
