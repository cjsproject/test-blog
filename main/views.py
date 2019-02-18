from django.shortcuts import render, get_object_or_404, render_to_response
from main.models import Blog, Category
# Create your views here.

def index(request):
    return render(request, 'index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, title):
    return render(request, 'view_post.html', {
        'post': get_object_or_404(Blog, slug=title)
    })

def view_category(request, title):
    category = get_object_or_404(Category, slug=title)
    return render(request, 'view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5],
    })
