from django.db import models

# Create your models here.
class NewsModel(models.Model):
    title=models.CharField(max_length=100)
    editor=models.CharField(max_length=100,default="Swapnosiri blood bank")
    image=models.ImageField(upload_to='news/images/')
    news=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)