from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = RichTextUploadingField(null=True)
    image = models.ImageField(upload_to='uploads/categories/', null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    posts_count = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = RichTextUploadingField(null=True)
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
    content = RichTextUploadingField(null=True)
    excerpt = RichTextUploadingField(null=True)
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

    def get_absolute_url(self):
        return reverse('blog:single-blog', kwargs={'pk': self.id})


class Comment(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = "PE", _("در انتظار تایید")
        PUBLISHED = "PU", _("تائید شده")
        REJECTED = "RE", _("رد شده")
        SPAM = "SP", _("هرزنامه")

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=StatusChoices, default=StatusChoices.PENDING)
    def get_absolute_url(self):
        return reverse('blog:single-blog', kwargs={'pk': self.post.id})

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f'{self.post.title}'
