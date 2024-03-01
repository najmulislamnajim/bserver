from django.shortcuts import render
from rest_framework import viewsets
from .models import NewsModel
from .serializer import NewsSerializer
# Create your views here.

class NewsViewSet(viewsets.ModelViewSet):
    queryset=NewsModel.objects.all()
    serializer_class=NewsSerializer