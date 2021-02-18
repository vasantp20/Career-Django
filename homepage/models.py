from django.db import models
from django.urls import reverse
import datetime
#from ckeditor.fields import RichTextField
# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name

 
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    tags = models.ManyToManyField(Tag)
    slug = models.SlugField(null=False, unique=True)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
