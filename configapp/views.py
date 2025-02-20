from django.shortcuts import render
from unicodedata import category

from .models import *



def yangi(request):
    news = News.objects.all()
    category = Category.objects.all()
    context = {
        'news': news,
        "title": "News",
        "category":category,

    }
    return render(request, 'Newsx/yangi.html', context=context)


