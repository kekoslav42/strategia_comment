from rest_framework import serializers

from post.models import Comment, Post


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostViewSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()

    def get_comment_count(self, obj):
        """ Добавляет количество комментариев к посту"""
        return obj.comment_count

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('lft', 'rght', 'tree_id')
        read_only_fields = ('comments',)

    def validate(self, data):
        """
        Валидация того что комментарий привязывается
        к родителю и относится к тому же посту что и родитель
        """
        if (data['parent'] is not None
                and data['parent'].post.id != data['post'].id):
            raise serializers.ValidationError(
                {"Error": "The comment (parent) does not belong to this post"}
            )

        return data
