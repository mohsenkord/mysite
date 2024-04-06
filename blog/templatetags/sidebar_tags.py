from ..models import Post,Category
from django import template

register = template.Library()


@register.inclusion_tag('blog/include/post-category.html')
def post_category():
    posts = Post.objects.filter(status='PU')
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(categories=name).count()
    return {'categories': cat_dict}


@register.inclusion_tag('blog/include/Latest-posts.html')
def latest_posts():
    return {'posts': Post.objects.filter(status='PU')[0:1]}