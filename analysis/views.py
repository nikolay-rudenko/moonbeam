from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from .models import Problem, Solution

def index(request):
    template = loader.get_template('analysis/index.html')
    prb = Problem.objects.all()
    slt = Solution.objects.all()
    context = {'prb': prb, 'slt': slt}

    return HttpResponse(template.render(context, request))