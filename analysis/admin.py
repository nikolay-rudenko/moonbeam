from django.contrib import admin

from .models import Problem, Solution

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'risks', 'description','parts', 'causes', 'published')
    list_display_links = ('title', 'risks', 'description')
    search_fields = ('title', 'description',)


class SolutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'problem', 'research', 'solutions', 'resources', 'plan', 'test')
    list_display_links = ('problem','research', 'solutions', 'resources')
    search_fields =('problem__title', 'research', 'solutions')

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SolutionAdmin)
