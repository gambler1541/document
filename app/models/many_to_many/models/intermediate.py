from django.db import models
__all__ = (
    'Person',
    'Group',
    'Membership',
)
class Person(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group','person'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person,
                               on_delete=models.CASCADE,
                               related_name='memberships')
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    recommender = models.ForeignKey(Person,
                                    related_name='memberships_by_recommender',
                                    on_delete=models.SET_NULL,
                                    blank=True,
                                    null=True)
    date_joined = models.DateTimeField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return '{person} - {group}({date})'.format(
            person = self.person,
            group = self.group,
            date = self.date_joined,
        )
