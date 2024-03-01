from django.shortcuts import render
from rest_framework import viewsets
from .models import BlogModel
from .serializer import BlogSerializer

# Create your views here.
class BlogViewSet(viewsets.ModelViewSet):
    queryset=BlogModel.objects.all()
    serializer_class=BlogSerializer