from django.contrib import admin

from .models import Problem, Solution


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'parts', 'causes', 'published')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'description',)


class SolutionAdmin(admin.ModelAdmin):
    list_display = ('problem', 'research', 'solutions', 'plan', 'test')
    list_display_links = ('problem','research', 'solutions')
    search_fields =('problem__title', 'research', 'solutions')


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Solution, SolutionAdmin)
