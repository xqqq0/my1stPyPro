from django.shortcuts import render
import  models

def index0(request):
    article = models.Article.objects.get(pk=1)
    return render(request, "blog/index.html", {"article": article})

def index(request):
    articles = models.Article.objects.all()
    return render(request,"blog/index.html", {"articles": articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,"blog/article_page.html",{"article":article})
