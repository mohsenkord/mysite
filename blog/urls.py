from django.urls import path
from .views import BlogListView, BlogDetailView, post_filter, PostSearchListView

app_name = 'blog'


urlpatterns = [
    path('', BlogListView.as_view(), name='index'),
    path('search/', PostSearchListView.as_view(), name='blog-search'),
    path('author/<str:author_username>/', post_filter, name='post_filter_author'),
    path('category/<str:category_slug>/', post_filter, name='post_filter_category'),
    path('tag/<str:tag_slug>/', post_filter, name='post_filter_tag'),
    path('<int:pk>/', BlogDetailView.as_view(), name='single-blog'),

]