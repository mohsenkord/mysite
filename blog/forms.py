from django import forms
from .models import Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('subject', 'content')
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        # Access user from the view (if needed)
        user = kwargs.get('user')
        if user:
            # self.initial['name'] = user.username
            # self.initial['email'] = user.email
            self.fields['name'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['readonly'] = True
        else:
            self.initial['name'] = 'Anonymous'
            self.initial['email'] = 'anpch@example.com'

