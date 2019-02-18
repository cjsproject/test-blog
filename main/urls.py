from django.urls import path
from .views import view_post, view_category, index
urlpatterns = [
    path('home/', index),

    path(
        'blog/view/<title>',
        view_post,
        name='view_blog_post'),
    path(
        'blog/category/<title>',
        view_category,
        name='view_blog_category'),
]
