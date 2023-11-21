from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User 


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    

# Create your models here.
class Post(models.Model):

    class Meta:
        ordering = ['-publish']
        indexes =[
            models.Index(fields=['-publish']),
        ]
    
    objects= models.Manager() #the default manager
    published =PublishedManager() # our custom manager
    
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    
    title = models.CharField(max_length=200)
    class Status(models.TextChoices):
        DRAFT = 'DF' ,'DAFT'
        PUBLISHED = 'PB', 'PUBLISHED'
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250 , unique_for_date='publish')
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status= models.CharField(max_length=2, 
                             choices=Status.choices,
                             default=Status.DRAFT)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',
                             args=[self.publish.year,
                             self.publish.month,
                             self.publish.day,
                             self.slug])        

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey('Post',
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80, blank=True)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created']),
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'