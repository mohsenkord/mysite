from django.shortcuts import render
from django.views import generic
from .forms import ContactForm, NewsletterForm
from .models import Contact, Newsletter


# Create your views here.


class IndexView(generic.TemplateView):
    template_name = 'website/index.html'


class AboutView(generic.TemplateView):
    template_name = 'website/about.html'


class ContactView(generic.FormView):
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class NewsletterView(generic.FormView):
    template_name = 'website/index.html'
    form_class = NewsletterForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
