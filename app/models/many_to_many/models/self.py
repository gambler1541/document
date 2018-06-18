from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    # 관계가 대칭적으로 형성됨
    #   A가 B를 friends에 추가 -> B의 friends에도 A가 추가되어있
    friends = models.ManyToManyField(
        'self',
    )

    def __str__(self):
        return self.name

    def show_friends(self):
        print(f'{self.name}의 친구목록')
        for friend in self.friends.all():
            print(f'- {friend.name}')
        print(f'총 ({len(self.friends.all())}명)')





