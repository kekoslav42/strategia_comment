from rest_framework import viewsets

from api.serializers import CommentSerializer, PostSerializer, CommentReadySerializer
from post.models import Comment, Post


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


    def perform_create(self, serializer):
        serializer.save()
