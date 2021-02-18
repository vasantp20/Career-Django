from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Article
from django.views.generic import ListView, DetailView
# Create your views here.

async def career(request):
    now = datetime.datetime.now()
    return render(request=request, template_name="main/homepage.html")


class ArticleListView(ListView):
    model = Article
    template_name = 'main/article_list.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'main/article_detail.html'
