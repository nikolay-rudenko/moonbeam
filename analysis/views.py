from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView
from .models import Problem, Solution
from django.http import HttpResponseRedirect
from .forms import ProblemForm, SolutionForm
from django.shortcuts import render


def index(request):
    template = loader.get_template('analysis/index.html')
    prb = Problem.objects.select_related()
    slt = Solution.objects.select_related()
    context = {'prb': prb, 'slt': slt}

    return HttpResponse(template.render(context, request))


class ProblemCreate(CreateView):
    model = Problem
    template_name = 'analysis/create.html'
    fields = ['title', 'risks', 'description', 'parts', 'causes']

    def post(self, request, *args, **kwargs):
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/saved/')

        return render(request, self.template_name, {'form': form})

class UpdateProblem(UpdateView):
        model = Problem
        template_name = 'analysis/update_problem.html'
        fields = ['title', 'risks', 'description', 'parts', 'causes']

        def post(self, request, *args, **kwargs):
            form = ProblemForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return HttpResponseRedirect('/saved/')

            return render(request, self.template_name, {'form': form})


class SolutionCreate(CreateView):
    model = Solution
    template_name = 'analysis/create.html'
    fields = ['problem', 'research', 'solutions', 'resources', 'plan', 'test']

    def post(self, request, *args, **kwargs):
        form = SolutionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/saved/')

        return render(request, self.template_name, {'form': form})




def saved(request):
    template = loader.get_template('analysis/saved.html')
    prb = Problem.objects.select_related()
    context = {'prb': prb,}

    return HttpResponse(template.render(context, request))


def delete(request, problem_id=None):
    # import pdb
    # pdb.set_trace()
    problem_to_delete = Problem.objects.get(pk=problem_id)
    problem_to_delete.delete()

    return HttpResponse(index(request))

# the solution to update problem on main page
def problenUpdateView(request, problem_id=None):
    # model = Problem
    # fields = ['title', 'risks', 'description']
    # template_name_suffix = '_update_form'

    problem_to_update = Problem.objects.get(pk=problem_id)
    # import pdb
    # pdb.set_trace()
    problem_to_update.title = 'Name changed again 3'
    problem_to_update.save()

    return HttpResponse(index(request))



