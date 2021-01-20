from django.contrib.auth.models import User, Group
from .models import Author, Article, ToyError
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'email']

