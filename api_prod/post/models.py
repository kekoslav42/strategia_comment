from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Post(models.Model):
    author = models.CharField(
        max_length=122,
        null=True,
        blank=True,
        default='Anonymous',
    )
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        default='Not title'
    )
    text = models.CharField(
        max_length=200
    )
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.title}: {self.text}'


class Comment(MPTTModel):
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    title = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        default='Not title'
    )
    author = models.CharField(
        max_length=122,
        null=True,
        blank=True,
        default='Anonymous',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    published = models.DateTimeField(
        auto_now_add=True
    )
