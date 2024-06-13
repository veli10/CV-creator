from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings 
from django.utils import translation 
from django.urls.base import resolve, reverse 
from django.urls.exceptions import Resolver404 
from urllib.parse import urlparse

# Create your views here.
def home__view(request):
    return render(request, 'home.html')

def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response