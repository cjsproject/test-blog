from django.db import models
from django.urls import reverse
# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('main.Category', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('view_blog_post', args={self.slug})

    def __str__(self):
        return "%s" % self.title

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('view_blog_category', args={self.slug})
