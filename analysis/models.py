from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, Blank=True)
    part_1 = models.TextField(null=True, Blank=True)
    part_2 = models.TextField(null=True, Blank=True)
    part_3 = models.TextField(null=True, Blank=True)
    cause_1 = models.TextField(null=True, Blank=True)
    cause_2 = models.TextField(null=True, Blank=True)
    cause_3 = models.TextField(null=True, Blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)

class Solution(models.Model):
    solution_1 = models.TextField(null=True, Blank=True)
    solution_2 = models.TextField(null=True, Blank=True)
    solution_3 = models.TextField(null=True, Blank=True)
    probability = models.FloatField(null=True, blank=True)
    plan = models.TextField(null=True, Blank=True)

class Reflection(models.Model):
    result = models.TextField(null=True, Blank=True)
    solution_pattern = models.TextField(null=True, blank=True)
    principles = models.TextField(null=True, blank=True)



