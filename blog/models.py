from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    slug=models.SlugField()
    intro=models.TextField()
    body=models.TextField()
    posted_date=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post=models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    body=models.CharField(max_length=200)
    posted_date = models.DateTimeField(auto_now_add=True)