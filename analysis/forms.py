from django.forms import ModelForm
from .models import Problem, Solution

class AnalysisProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = {'title', 'risks', 'description', 'parts', 'causes'}