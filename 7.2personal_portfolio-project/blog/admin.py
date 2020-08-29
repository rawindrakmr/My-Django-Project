from django.contrib import admin
from blog.models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display=['title','date']

admin.site.register(Blog,BlogAdmin)
