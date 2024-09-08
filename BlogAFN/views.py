from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied



# Create your views here.

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class ArticleViewSet(viewsets.ModelViewSet):

    # Ensure a user sees only own Note objects.
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Article.objects.filter(owner=user)
        raise PermissionDenied()

    # Set user as owner of a Notes object.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

