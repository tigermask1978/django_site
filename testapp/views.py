# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from .models import Document, Article
from django.forms import formset_factory
from .forms import DocumentForm, NameForm, ContactForm, ArticleForm
# Create your views here.


@require_http_methods(["GET", "POST"])
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>现在时间是：%s.</body></html>" % now
    return HttpResponse(html)


def list(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            return HttpResponseRedirect(reverse('test:list'))
    else:
        form = DocumentForm()

    documents = Document.objects.all()

    context = {'documents': documents, 'form': form}
    return render(request, 'testapp/list.html', context)


def myview(request):
    a = get_object_or_404(Article, pk=2)
    return redirect(a)


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            HttpResponseRedirect(request, reverse('test:your-name'))
    else:
        form = NameForm()

    return render(request, 'testapp/name.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['18931890131@189.cn']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'testapp/contact.html', {'form': form})


def manage_articles(request):
    ArticleFormSet = formset_factory(ArticleForm, extra=3)
    if request.method == 'POST':
        formset = ArticleFormSet(request.POST, request.FILES)
        if formset.is_valid():
            pass
    else:
        formset = ArticleFormSet()

    return render(request, 'testapp/manage_articles.html', {'formset': formset})