from django.urls import path
from analysis.views import index, AnCreateView

urlpatterns = [
    path('add/', AnCreateView.as_view(), name='add'),
    path('', index, name='index'),
]