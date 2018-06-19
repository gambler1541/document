from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    """
    User간의 관계는 2종류로 나뉨
        follow
        block

        관계를 나타내는 Relation클래스 사용 (중계모델)

    """
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField('self',
                                       symmetrical=False,
                                       through='Relation',
                                       )

    def __str__(self):
        return self.name


    @property
    def following_relations(self):
        return self.related_from_user.filter(relation_type='f')
        # return Relation.objects.filter(from_user=self, relation_type='f')

    @property
    def follower_relations(self):
        return self.related_to_user.filter(relation_type='f')

    @property
    def block_relations(self):
        return self.related_from_user.filter(relation_type='b')
        # return Relation.objects.filter(from_user=self, relation_type='b')

class Relation(models.Model):
    """
    TwitterUser 간의 MTM관계를 정의
        from_user
        to_user
        follow인지, block인지를 판단
    """
    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(TwitterUser,
                                  on_delete=models.CASCADE,
                                  related_name='related_from_user')
    to_user = models.ForeignKey(TwitterUser,
                                on_delete=models.CASCADE,
                                related_name='related_to_user')
    relation_type = models.CharField(
        max_length=1,
        choices=CHOICES_RELATION_TYPE,
    )
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        # get_FOO_display() 함수를 사용해서 choices를 사용한 필드의 출력값을 사용
        return 'from({}), to({}), {}'.format(
            self.from_user.name,
            self.to_user.name,
            self.get_relation_type_display(),
        )