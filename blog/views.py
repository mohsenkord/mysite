from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Post, Category, Tag, Comment
from .forms import CommentForm


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


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'blog/blog-single.html'
    form_class = CommentForm

    def get_object(self, queryset=None):
        return get_object_or_404(Post, pk=self.kwargs.get('pk'))

    def form_valid(self, form):
        self.object = form.save(commit=False)  # Save the comment but don't commit yet
        self.object.post = self.get_object()  # Assign the comment to the current post
        self.object.save()  # Now save the comment with the assigned post
        return redirect('blog:single-blog', pk=self.object.post.pk)


class CommentListView(generic.ListView):
    template_name = 'blog/blog-single.html'
    model = Comment
    context_object_name = 'comments_list'

    def get_queryset(self):
        post_pk = self.kwargs.get('pk')
        if post_pk is not None:
            # Efficiently fetch the post and filter comments
            comment = Comment.objects.filter(post__pk=post_pk)
            return comment.filter(status='PU').order_by('-created_at')
        else:
            # Handle case where no post ID is provided (optional)
            return Comment.objects.none()
