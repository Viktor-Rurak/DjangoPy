from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Article, Category
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Article, Category

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        articles = Article.objects.all()
        categories = Category.objects.all()

        context = {
            'articles': articles,
            'categories': categories
        }

        return render(request, self.template_name, context)


class ArticleDetailView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        return render(request, 'article_detail.html', {'article': article})


class CategoryArticlesView(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        articles = category.articles.all()

        return render(request, 'category_articles.html', {
            'category': category,
            'articles': articles
        })
