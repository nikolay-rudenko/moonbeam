from django.urls import path
from analysis.views import index, saved, delete, UpdateProblem, ProblemCreate, SolutionCreate

urlpatterns = [
    path('addpr/', ProblemCreate.as_view(), name='addpr'),
    path('edit/<pk>', UpdateProblem.as_view(), name='update_problem'),
    path('addsl/', SolutionCreate.as_view(), name='addsl'),
    path('saved/', saved, name='saved'),
    path('delete/<problem_id>', delete, name='delete'),
    path('', index, name='index'),
]