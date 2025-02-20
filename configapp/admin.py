from django.contrib import admin
from .models import News, Category

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'context', 'is_bool', ' photo', 'category')
    list_display_links = ('title', 'context')
    search_fields = ['title']

admin.site.register(News)
admin.site.register(Category)
