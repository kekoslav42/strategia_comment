from django.urls import path, include

from api import views
from rest_framework.routers import DefaultRouter

v1_router = DefaultRouter()
v1_router.register(r'posts', views.PostViewSet, basename='posts')
v1_router.register(r'comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(v1_router.urls)),
]
