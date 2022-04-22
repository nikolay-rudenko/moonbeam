from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView
from .models import Problem, Solution
from django.http import HttpResponseRedirect
from .forms import ProblemForm, SolutionForm
from django.shortcuts import render

# starting page, third commit 
def index(request):
    template = loader.get_template('analysis/index.html')
    prb = Problem.objects.select_related()
    slt = Solution.objects.select_related()
    context = {'prb': prb, 'slt': slt}

    return HttpResponse(template.render(context, request))


class ProblemCreate(CreateView):
    model = Problem
    template_name = 'analysis/create.html'
    fields = ['title', 'description', 'parts', 'causes', 'risks']

    def post(self, request, *args, **kwargs):
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/saved/')

        return render(request, self.template_name, {'form': form})


class UpdateProblem(UpdateView):
    model = Problem
    template_name = 'analysis/update_problem.html'

    fields = ['title', 'description', 'parts', 'causes', 'risks']

    def post(self, request, *args, **kwargs):
        form = ProblemForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/updated_problem/')

        return render(request, self.template_name, {'form': form})


class SolutionCreate(CreateView):
    model = Solution
    template_name = 'analysis/create_solution.html'

    fields = [
        'problem',
        'research',
        'solutions',
        'resources',
        'plan',
        'test'
    ]

    def post(self, request, *args, **kwargs):
        form = SolutionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/saved/')

        return render(request, self.template_name, {'form': form})
    
    def get_context_data(self, *args, **kwargs):
        # template = loader.get_template('analysis/updated_problem.html')
        prb = Problem.objects.select_related()
        context = {'prb': prb}
  
        return render(self.request, self.template_name, context)


class UpdateSolution(UpdateView):
    model = Solution
    template_name = 'analysis/update_solution.html'

    fields = [
        'problem',
        'research',
        'solutions',
        'resources',
        'plan',
        'test'
    ]

    def post(self, request, *args, **kwargs):
        form = SolutionForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/updated_solution/')

        return render(request, self.template_name, {'form': form})


def saved(request):
    template = loader.get_template('analysis/saved.html')
    prb = Problem.objects.select_related()
    slt = Solution.objects.select_related()

    context = {'prb': prb, 'slt': slt}

    return HttpResponse(template.render(context, request))


def updated_problem(request):
    template = loader.get_template('analysis/updated_problem.html')
    prb = Problem.objects.select_related()
    context = {'prb': prb, }

    return HttpResponse(template.render(context, request))


def updated_solution(request):
    template = loader.get_template('analysis/updated_solution.html')
    slt = Solution.objects.select_related()
    context = {'slt': slt, }

    return HttpResponse(template.render(context, request))


def delete_problem(request, problem_id=None):
    problem_to_delete = Problem.objects.get(pk=problem_id)
    problem_to_delete.delete()

    return HttpResponse(index(request))


def delete_solution(request, solution_id=None):
    solution_to_delete = Solution.objects.get(pk=solution_id)
    solution_to_delete.delete()

    return HttpResponse(index(request))
