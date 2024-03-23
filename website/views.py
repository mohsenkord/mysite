from django.shortcuts import render
from django.views import generic


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'website/index.html'


class ContactView(generic.TemplateView):
    template_name = 'website/contact.html'


class AboutView(generic.TemplateView):
    template_name = 'website/about.html'
