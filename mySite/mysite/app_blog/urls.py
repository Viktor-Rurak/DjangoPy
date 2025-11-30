from django.urls import path
from .views import HomePageView, ArticleDetailView, CategoryArticlesView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('category/<slug:slug>/', CategoryArticlesView.as_view(), name='category_articles'),
]
