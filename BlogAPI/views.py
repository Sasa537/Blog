from django.shortcuts import render
from WebBlog.models import Articles
from rest_framework import generics
from . import serializers


class ArticlesList(generics.ListAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticleSerializer


class ArticlesDetail(generics.RetrieveAPIView):
    queryset = Articles.objects.all()
    serializer_class = serializers.ArticleSerializer



















