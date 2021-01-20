from django.contrib.auth.models import User, Group
from django.http import JsonResponse, HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from deccra.terminal_1.serializers import AuthorSerializer
from .models import Article, Author, ToyError


class ArticleView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

class ToysView(APIView):
    def get(self, request):
        toys = ToyError.objects.all()
        return Response({"toys": toys})