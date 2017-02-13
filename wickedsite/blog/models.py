from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(max_length=50)
    posted_at = models.DateTimeField('Posted at : ', auto_now_add=True)
