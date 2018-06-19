from django.db import models

__all__ = (
    'RelatedUser',
    'PostBase',
    'PhotoPost',
    'TextPost',
)

class RelatedUser(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PostBase(models.Model):
    author = models.ForeignKey(
        RelatedUser,
        on_delete=models.CASCADE,
        # abstract_base_classes_photopost
        # related_name='%(app_label)s_%(class)s',
        related_name='%(class)ss',

    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class PhotoPost(PostBase):
    # related_name : photoposts
    photo_url = models.CharField(max_length=500)

    #related_name : textposts
class TextPost(PostBase):
    text = models.TextField()

