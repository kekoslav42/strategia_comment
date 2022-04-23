from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api_v2 import views

v2_router = DefaultRouter()
v2_router.register(r'posts', views.PostViewSet, basename='posts')
v2_router.register(r'comments', views.CommentViewSet, basename='comments')

urlpatterns = [
    path('', include(v2_router.urls)),
]
