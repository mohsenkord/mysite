from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post


class LatestEntriesFeed(Feed):
    title = "blog newest posts"
    link = "rss/feeds/"
    description = ""

    def items(self):
        return Post.objects.filter(status='PU')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.excerpt[0:100]
