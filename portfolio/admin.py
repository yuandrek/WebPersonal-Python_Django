
from django.contrib import admin
from .models import proyecto
from .models import slider

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(proyecto, ProjectAdmin)
admin.site.register(slider)