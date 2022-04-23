from django.db.models import Count
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from api_v2.serializers import (CommentSerializer, PostCreateSerializer,
                                PostViewSerializer)
from api_v2.services import generate_comment
from post.models import Comment, Post


class MyModelsViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    """
    Кастомный вьюсет на создание, получение списка объектов или одного объекта
    """
    pass


class PostViewSet(MyModelsViewSet):
    queryset = Post.objects.annotate(comment_count=Count('comments'))

    def get_serializer_class(self):
        """ Выбор класса сериализатора"""
        return (
            PostViewSerializer
            if self.request.method == 'GET'
            else PostCreateSerializer
        )


class CommentViewSet(MyModelsViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        """
        Возращает список всех комментариев
        """
        return Response(generate_comment(
            CommentSerializer(
                self.get_queryset(), many=True
            ).data
        ))

    def retrieve(self, request, *args, **kwargs):
        """
        Возращает список всех комментариев к посту
        """
        return Response(generate_comment(
            CommentSerializer(
                Comment.objects.filter(post=kwargs['pk']), many=True
            ).data
        ))
