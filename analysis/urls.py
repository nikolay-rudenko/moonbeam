from django.urls import path
from analysis.views import index, AnCreateView, saved

urlpatterns = [
    path('add/', AnCreateView.as_view(), name='add'),
    path('saved/', saved, name='saved'),
    path('', index, name='index'),
]