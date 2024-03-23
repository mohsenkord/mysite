from django.urls import path
from website.views import IndexView, AboutView, ContactView


app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
]