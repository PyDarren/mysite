from django.shortcuts import render, get_object_or_404
from .models import BlogAriticles

# Create your views here.
def blog_title(request):
    blogs = BlogAriticles.objects.all()
    return render(request, "blog/titles.html", {"blogs":blogs})

def blog_article(request, article_id):
    # article = BlogAriticles.objects.get(id=article_id)
    article = get_object_or_404(BlogAriticles, id=article_id)
    pub = article.publish
    return render(request, "blog/content.html",
                  {"article":article, "publish":pub})
