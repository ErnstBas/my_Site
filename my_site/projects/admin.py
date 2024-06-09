from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', id)
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)
