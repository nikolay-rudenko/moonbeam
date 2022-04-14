from django.urls import path
from analysis.views import index, saved, delete, updated_problem, UpdateProblem, ProblemCreate, SolutionCreate

urlpatterns = [
    path('addpr/', ProblemCreate.as_view(), name='addpr'),
    path('edit/<pk>', UpdateProblem.as_view(), name='update_problem'),
    path('addsl/', SolutionCreate.as_view(), name='addsl'),
    path('saved/', saved, name='saved'),
    path('updated_problem/', updated_problem, name='updated_problem'),
    path('delete/<problem_id>', delete, name='delete'),
    path('edit/home', index, name='index'),
    path('', index, name='index'),
]