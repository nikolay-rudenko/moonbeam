from django.forms import ModelForm, Textarea
from .models import Problem, Solution
from django import forms


class ProblemForm(ModelForm):
    class Meta:
        model = Problem
        fields = '__all__'


class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        fields = '__all__'

