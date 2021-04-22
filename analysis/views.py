from django.http import HttpResponse
from django.template import loader
from .models import Problem

def index(request):
    template = loader.get_template('analysis/index.html')
    prb = Problem.objects.get_queryset()
    context = {'prb': prb}

    return HttpResponse(template.render(context, request))

