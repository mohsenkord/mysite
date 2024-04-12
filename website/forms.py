from django import forms
from .models import Contact, Newsletter


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control common-input mb-20',
                                           'name': "name",
                                           'placeholder': 'Enter your name',
                                           'onfocus': "this.placeholder = ''",
                                           'onblur': "this.placeholder = 'Enter your name'",
                                           'required': "",
                                           'type': 'text',
                                           }),
            'email': forms.EmailInput(attrs={'class': 'form-control common-input mb-20',
                                             'name': "email",
                                             'placeholder': 'Enter email address',
                                             'onfocus': "this.placeholder = ''",
                                             'onblur': "this.placeholder = 'Enter email address'",
                                             'required': "",
                                             'type': 'email',
                                             'pattern': "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$"
                                             }),
            'subject': forms.TextInput(attrs={'class': 'form-control common-input mb-20',
                                              'name': "subject",
                                              'placeholder': 'Enter subject',
                                              'onfocus': "this.placeholder = ''",
                                              'onblur': "this.placeholder = 'Enter subject'",
                                              'required': "",
                                              'type': 'text',
                                              }),
            'message': forms.Textarea(attrs={'class': 'common-textarea form-control',
                                             'name': "message",
                                             'placeholder': 'Enter Message',
                                             'onfocus': "this.placeholder = ''",
                                             'onblur': "this.placeholder = 'Enter Message'",
                                             'required': "",
                                             'type': 'text', }),
        }


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control common-input mb-20',
                                             'name': "email",
                                             'placeholder': 'Enter email address',
                                             'onfocus': "this.placeholder = ''",
                                             'onblur': "this.placeholder = 'Enter email address'",
                                             'required': "",
                                             'type': 'email',
                                             'pattern': "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$"
                                             }),
        }
