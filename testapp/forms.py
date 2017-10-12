# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea
from testapp.models import Author, Book
from django.core.exceptions import NON_FIELD_ERRORS


class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )


class NameForm(forms.Form):
    your_name = forms.CharField(label='你的名字', max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']
        error_messages = {
            'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
        }
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']

