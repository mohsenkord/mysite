from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/categories/')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    posts_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField()
    color = models.CharField(max_length=7)
    image = models.ImageField(upload_to='uploads/tags/')
    posts_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Post(models.Model):
    class StatusChoices(models.TextChoices):
        DRAFT = "DR", _("پیش نویس")
        PUBLISHED = "PU", _("منتشر شده")

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    excerpt = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)
    publish_date = models.DateField()
    publish_time = models.TimeField()
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, choices=StatusChoices, default=StatusChoices.PUBLISHED)
    image = models.ImageField(upload_to='uploads/posts/')
    views = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)

    def __str__(self):
        return self.title