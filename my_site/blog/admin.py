from django.contrib import admin

# Register your models here.
from .models import Blog

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'date')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, ProjectAdmin)



