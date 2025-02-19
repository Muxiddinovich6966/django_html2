from django.contrib import admin
# from .models import Kurs, Student
from .models import News



class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'context', 'is_bool', ' photo')
    list_display_links = ('title', 'context')
    search_fields = ['title']

admin.site.register(News)
