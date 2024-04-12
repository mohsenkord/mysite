from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(null=True, )
    image = models.ImageField(upload_to='uploads/categories/', null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    posts_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(null=True)
    color = models.CharField(max_length=7, null=True)
    image = models.ImageField(upload_to='uploads/tags/', null=True)
    posts_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = "DR", _("پیش نویس")
        PUBLISHED = "PU", _("منتشر شده")

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField(null=True)
    excerpt = models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=StatusChoices, default=StatusChoices.PUBLISHED)
    image = models.ImageField(upload_to='uploads/posts/', null=True)
    views = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    ordering = ('-publish_date', '-publish_time')

    def __str__(self):
        return self.title
