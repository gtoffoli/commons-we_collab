from django.shortcuts import render
from django.contrib.flatpages.models import FlatPage

def home(request):
    # return HttpResponseRedirect('/project/we-collab/')
    return render(request, 'flatpages/splash.html', {'flatpage': FlatPage.objects.get(url='/we-collab/cover/')})
