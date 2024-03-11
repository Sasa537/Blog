from django.shortcuts import render
from .models import Articles
from django.core.paginator import Paginator
from django.views.generic import DetailView

class ArticleDetailViews(DetailView):
    model = Articles
    template_name = 'webblog/article_views.html'
    context_object_name = 'article'


def index(request):
    articles = Articles.objects.all()
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'webblog/index.html', {'page_obj': page_obj})


def about(request):
    return render(request, 'webblog/about.html')


def contacts(request):
    return render(request, 'webblog/contacts.html')
