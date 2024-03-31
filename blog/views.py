from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# Create your views here.
class BlogListView(generic.ListView):
    template_name = 'blog/blog-home.html'
    queryset = Post.objects.filter(status='PU')
    context_object_name = 'blog_list'


class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog-single.html'
    pk_url_kwarg = 'pk'
    query_pk_and_slug = True
