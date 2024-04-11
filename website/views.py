from django.shortcuts import render
from django.views import generic
from .models import ContactUs

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'website/index.html'


class AboutView(generic.TemplateView):
    template_name = 'website/about.html'


class ContactView(generic.FormView):
    template_name = 'website/contact.html'
    form_class = ContactUs
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

