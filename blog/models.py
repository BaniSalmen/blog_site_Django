from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    class status(models.TextChoices):
        DRAFT = 'DF' ,'DAFT'
        PUBLISHED = 'PB', 'PUBLISHED'
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status= models.CharField(max_length=2, 
                             choices=status.choices,
                             default=status.DRAFT)