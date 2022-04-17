from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api import views

v1_router = DefaultRouter()
v1_router.register(r'posts', views.PostViewSet, basename='posts')
v1_router.register(r'comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(v1_router.urls)),
]
