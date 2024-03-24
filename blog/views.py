from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# Create your views here.
class BlogListView(generic.ListView):
    template_name = 'blog/blog-home.html'
    context_object_name = 'blog_list'


class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog-single.html'

