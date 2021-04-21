from django.db import models


class Goal(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(null=True, Blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

class Problem(models.Model):
    problem = models.ForeignKey(Goal, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(null=True, Blank=True)
    parts = models.TextField(null=True, Blank=True)
    causes = models.TextField(null=True, Blank=True)
    description = models.TextField(null=True, Blank=True)

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    research = models.TextField(null=True, Blank=True)
    solutions = models.TextField(null=True, Blank=True)
    probability = models.FloatField(null=True, blank=True)
    plan = models.TextField(null=True, Blank=True)

class Reflection(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    result = models.TextField(null=True, Blank=True)
    problem_pattern = models.TextField(null=True, Blank=True)
    solution_pattern = models.TextField(null=True, blank=True)
    principles = models.TextField(null=True, blank=True)



