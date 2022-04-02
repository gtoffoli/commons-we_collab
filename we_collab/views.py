from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage

def cover(request):
    return render(request, 'flatpages/splash.html', {'flatpage': FlatPage.objects.get(url='/we-collab/cover/')})

def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/project/we-collab/')
    else:
        return cover(request)
