from django.contrib import admin
from .models import Article, Tag
# Register your models here.
admin.site.register(Tag)
admin.site.register(Article)