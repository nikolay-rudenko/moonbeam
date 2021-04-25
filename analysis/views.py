from django.http import HttpResponse
from django.template import loader
from .models import Problem, Solution

def index(request):
    template = loader.get_template('analysis/index.html')
    prb = Problem.objects.all().order_by('published')
    slt = Solution.objects.get_queryset().order_by('id')
    context = {'prb': prb, 'slt': slt}

    return HttpResponse(template.render(context, request))

