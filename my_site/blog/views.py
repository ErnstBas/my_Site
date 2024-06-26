import requests
from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView, DetailView

class BlogListView(ListView):
    template_name = "blog/blog_list.html"
    model = Blog #refer to models.py
    context_object_name = "blog"
    
class SingleBlogView(DetailView):
    template_name = "blog/blog_post.html"
    model = Blog
    #indicate slug or pk in urlpatterns