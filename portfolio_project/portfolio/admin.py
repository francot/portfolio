from django.contrib import admin
from portfolio.models import Job, JobCategory


class JobAdmin (admin.ModelAdmin):
    list_display = ('title', 'date')


# Register your models here.

admin.site.register(Job, JobAdmin)
admin.site.register(JobCategory)
