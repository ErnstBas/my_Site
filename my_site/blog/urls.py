from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from .views import BlogListView, SingleBlogView  # Import BlogListView

urlpatterns = [
    path("", BlogListView.as_view(), name="blog_list"),
    path("<slug:slug>/", SingleBlogView.as_view(), name="blog_post"),
]

