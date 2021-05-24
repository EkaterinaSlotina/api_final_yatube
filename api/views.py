from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.generics import get_object_or_404

from .customviewset import ListCreateBasicViewSet
from .models import Post, Group, User
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer
)


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('group',)

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(ListCreateBasicViewSet):
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'following__username')

    def get_queryset(self):
        follower = get_object_or_404(User, pk=self.request.user.pk)
        return follower.following.all()


class GroupViewSet(ListCreateBasicViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
