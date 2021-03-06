from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import PostsViewSet, CommentViewSet, GroupViewSet, FollowViewSet

v1_router = DefaultRouter()
v1_router.register(r'group', GroupViewSet, basename='group')
v1_router.register(r'posts', PostsViewSet, basename='posts'),
v1_router.register(
    r'posts/(?P<id>\d+)/comments',
    CommentViewSet, basename='comments'
)
v1_router.register(r'follow', FollowViewSet, basename='follow'),


urlpatterns = [
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path(
        'v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'
    ),
    path('v1/', include(v1_router.urls)),
]
