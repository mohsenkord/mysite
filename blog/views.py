from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post, Category, Tag


# Create your views here.
class BlogListView(generic.ListView):
    template_name = 'blog/blog-home.html'
    queryset = Post.objects.filter(status='PU').order_by('-publish_date')
    paginate_by = 1
    context_object_name = 'posts'


class BlogDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/blog-single.html'
    pk_url_kwarg = 'pk'


def post_filter(request, category_slug=None, tag_slug=None, author_username=None):
    author = None
    object_list = Post.objects.filter(status='PU').order_by('-publish_date')
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

    paginator = Paginator(object_list, 1)  # 2 posts in each page
    page = request.GET.get('page')

    try:
        object_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        object_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        object_list = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post-filter.html',
                  {'category': category,
                   'tag': tag,
                   'author': author,
                   'object_list': object_list,
                   'page_obj': page})


class PostSearchListView(generic.ListView):
    template_name = 'blog/post-search.html'
    paginate_by = 1
    model = Post

    def get_queryset(self):
        name = self.request.GET.get('q', '')
        object_list = self.model.objects.filter(status='PU').order_by('-publish_date')

        if name:
            object_list = object_list.filter(
                Q(title__icontains=name) |
                Q(content__icontains=name))
        else:
            object_list = object_list.none()
        return object_list

