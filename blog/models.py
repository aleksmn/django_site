from django.db import models

# Create your models here.
class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.title
    



