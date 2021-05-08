from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Problem, Solution
from .forms import AnalysisProblemForm

def index(request):
    template = loader.get_template('analysis/index.html')
    prb = Problem.objects.all()
    slt = Solution.objects.all()
    context = {'prb': prb, 'slt': slt}

    return HttpResponse(template.render(context, request))

class AnCreateView(CreateView):
    template_name = 'analysis/create.html'
    form_class = AnalysisProblemForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Problem.objects.all()
        return context
