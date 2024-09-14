from django.contrib import admin
from .models import Project
from blog.models import Blog

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'id', 'date')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Project, ProjectAdmin)
