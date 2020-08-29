from django.contrib import admin
from portfolio.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=['title', 'description']

admin.site.register(Project,ProjectAdmin)