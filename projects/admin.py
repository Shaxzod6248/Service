from django.contrib import admin
from .models import Const_projects, WorkType, Photos


admin.site.register(WorkType)
admin.site.register(Const_projects)
admin.site.register(Photos)