from django.contrib import admin
from .models import Category, Article, ArticleImage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    prepopulated_fields = {'slug': ('category',)}

admin.site.register(Category, CategoryAdmin)

class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'main_page')
    list_filter = ('main_page', 'pub_date')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ArticleImageInline]

admin.site.register(Article, ArticleAdmin)
