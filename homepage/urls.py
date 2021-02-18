from django.contrib import admin
from django.urls import path, include
import homepage.views
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    path('career', homepage.views.career),
    path('', ArticleListView.as_view(), name='article_list'),
     path('article/<slug:slug>', ArticleDetailView.as_view(), name='article_detail'),
    
]