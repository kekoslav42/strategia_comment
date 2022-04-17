from django.conf import settings
from mptt.templatetags.mptt_tags import cache_tree_children
from rest_framework import serializers

from post.models import Comment, Post

class CommentSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField('get_children')

    def get_children(self, comment):
        max_level = settings.MAX_LEVEL
        children = comment.get_children()
        if all([max_level is not None, comment.get_level() >= max_level]):
            return []
        return CommentSerializer(
            children,
            many=True
        ).data

    class Meta:
        model = Comment
        exclude = ('lft', 'rght', 'tree_id')
        read_only_fields = ('comments',)


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField('get_comments')

    def get_comments(self, post):
        comments = cache_tree_children(
            Comment.objects.filter(
                post=post,
                level__lte=settings.MAX_LEVEL
            )
        )
        serializer = CommentSerializer(
            comments,
            many=True
        )
        return serializer.data

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('comments',)
