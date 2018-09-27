from django.shortcuts import render

from articles.models import Article
from articles.serializers import ArticleSerializer
from rest_framework import generics

class ArticleListCreate(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

# Create your views here.
