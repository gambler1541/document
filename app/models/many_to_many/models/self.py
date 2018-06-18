from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    # 관계가 대칭적으로 형성됨
    #   A가 B를 friends에 추가 -> B의 friends에도 A가 추가되어있음
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name