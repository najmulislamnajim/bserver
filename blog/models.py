from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    image=models.ImageField(upload_to='blog/images/')
    blog=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)