from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=100, primary_key=True)
    description = models.TextField(null=True, blank=True)
    parts = models.TextField(null=True, blank=True)
    causes = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, editable=False)

class Solution(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    research = models.TextField(null=True, blank=True)
    solutions = models.TextField(null=True, blank=True)
    plan = models.TextField(null=True, blank=True)




