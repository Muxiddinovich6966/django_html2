from django.shortcuts import render
from .models import *



def yangi(request):
    talabalar = News.objects.all()
    news = News.objects.all()
    context = {
        "talabalar": talabalar,
        'news': news,
        "title": "News",
        "filtr": ['sport', 'texnologiya', 'siyosat', 'sogliq']

    }
    return render(request, 'Newsx/yangi.html', context=context)

