from django.contrib import admin
from .models import Post, Tag, Category, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'publish_date')
    list_filter = ('author', 'created_at', 'publish_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('tags',)
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post', 'created_at', 'status']
    list_filter = ('status', 'created_at')
    search_fields = ('author', 'content')
    date_hierarchy = 'created_at'
    ordering = ('status', 'created_at')
    actions = ['approve_comments']

    def has_add_permission(self, request):
        return False

    def approve_comments(self, request, queryset):
        return queryset.update(status='PU')

