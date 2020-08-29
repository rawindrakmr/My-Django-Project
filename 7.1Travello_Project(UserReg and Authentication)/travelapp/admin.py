from django.contrib import admin
from .models import Destination


class DestinationAdmin(admin.ModelAdmin):
    list_display=['name','desc']


admin.site.register(Destination, DestinationAdmin)