from django.shortcuts import render
from django.views.generic import ListView
from .models import PyArticles


class PyArticlesListView(ListView):
    model = PyArticles
    template_name = 'home.html'


def PyArticlesDetailView(request, pk):
    article = PyArticles.objects.get(id=pk)
    return render(request, 'article_detail.html', {'article': article})
