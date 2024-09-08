from .models import Article
from rest_framework import viewsets
from .serializers import ArticleSerializer



# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """
    queryset = Article.objects.all().order_by('-created_at')
    serializer_class = ArticleSerializer