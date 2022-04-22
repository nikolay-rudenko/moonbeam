from django.urls import path
from analysis.views import index, saved, delete_problem, delete_solution, updated_problem, updated_solution, UpdateProblem, ProblemCreate, SolutionCreate, UpdateSolution

urlpatterns = [
    path('addpr/', ProblemCreate.as_view(), name='addpr'),
    path('edit/<pk>', UpdateProblem.as_view(), name='update_problem'),
    path('addsl/', SolutionCreate.as_view(), name='addsl'),
    path('update_solution/<pk>', UpdateSolution.as_view(), name='update_solution'),
    path('updated_problem/', updated_problem, name='updated_problem'),
    path('updated_solution/', updated_solution, name='updated_solution'),
    path('delete/<problem_id>', delete_problem, name='delete_problem'),
    path('delete_solution/<solution_id>', delete_solution, name='delete_solution'),
    path('saved/', saved, name='saved'),
    path('edit/home', index, name='index'),
    path('', index, name='index'),
]