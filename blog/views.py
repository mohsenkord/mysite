from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category, Tag

# Create your views here.
class BlogListView(generic.ListView):
    template_name = 'blog/blog-home.html'
    queryset = Post.objects.filter(status='PU')
    context_object_name = 'posts'


class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog-single.html'
    pk_url_kwarg = 'pk'


def post_filter(request, category_slug=None, tag_slug=None, author_username=None):
    global author
    object_list = Post.objects.filter(status='PU')
    category = None
    tag = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        object_list = object_list.filter(categories=category)

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags=tag)

    if author_username:
        author = get_object_or_404(User, username=author_username)
        object_list = object_list.filter(author__username=author_username)

    return render(request,
                  'blog/post-filter.html',
                  {'category': category,
                   'tag': tag,
                   'author': author,
                   'object_list': object_list})


class PostSearchListView(generic.ListView):
    template_name = 'blog/post-search.html'
    model = Post

    def get_queryset(self):
        name = self.request.GET.get('q', '')
        object_list = self.model.objects.filter(status='PU')
        if name:
            object_list = object_list.filter(
                Q(title__icontains=name) |
                Q(context__icontains=name) |
                Q(tags__icontains=name) |
                Q(categories__icontains=name))
        return object_list
